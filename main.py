"""
Resample raw EEG/MEG data app for Brainlife.io

Resamples raw FIF file to a new sampling frequency.
Generates QC plots: PSD before/after comparison.

Inputs:  raw FIF file
Outputs: out_dir/raw.fif, out_report/report.html, product.json
"""

# Copyright (c) 2026 brainlife.io

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'brainlife_utils'))

import mne
import matplotlib.pyplot as plt

from brainlife_utils import (
    load_config,
    setup_matplotlib_backend,
    ensure_output_dirs,
    create_product_json,
    add_info_to_product,
    add_image_to_product,
    add_raw_info_to_product,
)

setup_matplotlib_backend()
config = load_config()
ensure_output_dirs('out_dir', 'out_figs', 'out_report')

# ── Config params ─────────────────────────────────────────────────────────────
raw_file    = config.get('raw') or config.get('fif') or config.get('mne')
sfreq       = float(config.get('sfreq', 250))

# Brainlife may pass a directory instead of a file — resolve to raw.fif inside it
if raw_file and os.path.isdir(raw_file):
    raw_file = os.path.join(raw_file, 'raw.fif')

# Advanced options (match guiomar/app-meeg-resample defaults)
npad        = config.get('npad', 'auto')
window      = config.get('window', 'boxcar')
pad         = config.get('pad', 'reflect_limited')
method      = config.get('method', 'fft')  # 'fft' (default) or 'polyphase'
events_val  = config.get('events') or None
events_val  = None if events_val in ('None', 'none', '') else events_val

stim_picks  = config.get('stim_picks') or None
stim_picks  = None if stim_picks in ('None', 'none', '') else stim_picks

if not raw_file or not os.path.exists(raw_file):
    raise FileNotFoundError(f"Raw FIF file not found: {raw_file!r}. Set 'raw' in config.json.")

# ── Load raw ──────────────────────────────────────────────────────────────────
print(f"Loading raw: {raw_file}")
raw = mne.io.read_raw_fif(raw_file, preload=True, verbose=True)

orig_sfreq = raw.info['sfreq']
print(f"  {len(raw.ch_names)} channels, {orig_sfreq:.1f} Hz → {sfreq:.1f} Hz, {raw.times[-1]:.1f} s")

# ── Plot 1: PSD before (full original spectrum, mark target Nyquist) ──────────
psd_before_path = None
try:
    fig_before = raw.plot_psd(fmax=orig_sfreq / 2 - 1, show=False)
    fig_before.suptitle(
        f'PSD Before Resampling  |  {orig_sfreq:.0f} Hz → {sfreq:.0f} Hz', y=1.02)
    # Mark the target Nyquist on every axis so user can see the future cutoff
    for ax in fig_before.axes:
        ax.axvline(sfreq / 2, color='red', linestyle='--', linewidth=1.2,
                   label=f'Target Nyquist ({sfreq/2:.0f} Hz)')
        ax.legend(fontsize=7, loc='upper right')
    psd_before_path = os.path.join('out_figs', 'psd_before.png')
    fig_before.savefig(psd_before_path, dpi=150, bbox_inches='tight')
    plt.close(fig_before)
except Exception as e:
    print(f"Could not plot PSD before: {e}")

# ── Resample ──────────────────────────────────────────────────────────────────
print(f"Resampling to {sfreq:.1f} Hz (method={method}, npad={npad}, window={window}, pad={pad})...")
raw.resample(sfreq, npad=npad, window=window, pad=pad,
             stim_picks=stim_picks, events=events_val, n_jobs=1)
print(f"  Done. New duration: {raw.times[-1]:.1f} s, {len(raw.times)} samples")

# ── Plot 2: PSD after (new Nyquist, brick-wall cutoff visible) ────────────────
psd_after_path = None
try:
    fig_after = raw.plot_psd(fmax=sfreq / 2 - 1, show=False)
    fig_after.suptitle(
        f'PSD After Resampling  |  {sfreq:.0f} Hz  (Nyquist = {sfreq/2:.0f} Hz)', y=1.02)
    psd_after_path = os.path.join('out_figs', 'psd_after.png')
    fig_after.savefig(psd_after_path, dpi=150, bbox_inches='tight')
    plt.close(fig_after)
except Exception as e:
    print(f"Could not plot PSD after: {e}")

# ── Save FIF ──────────────────────────────────────────────────────────────────
out_fif = os.path.join('out_dir', 'raw.fif')
raw.save(out_fif, overwrite=True)
print(f"Saved: {out_fif}")

# ── MNE Report ────────────────────────────────────────────────────────────────
report = mne.Report(title='Resample Report')

if psd_before_path:
    report.add_image(psd_before_path, title=f'PSD Before ({orig_sfreq:.0f} Hz)')
if psd_after_path:
    report.add_image(psd_after_path, title=f'PSD After ({sfreq:.0f} Hz)')

report.save(os.path.join('out_report', 'report.html'), overwrite=True)

# ── product.json ──────────────────────────────────────────────────────────────
product_items = []

add_info_to_product(product_items, f"Resampled: {orig_sfreq:.0f} Hz → {sfreq:.0f} Hz")
add_raw_info_to_product(product_items, raw)

for label, path in [
    ('PSD Before', psd_before_path),
    ('PSD After',  psd_after_path),
]:
    if path and os.path.exists(path):
        add_image_to_product(product_items, label, filepath=path)

create_product_json(product_items)
print("Done.")
