# app-resample-raw-v2

Brainlife app to resample raw EEG/MEG FIF data to a target sampling frequency using MNE-Python.

## Inputs

| ID | Datatype | Description |
|----|----------|-------------|
| `raw` | `neuro/meeg/mne/raw` | Raw FIF file to resample |

## Outputs

| ID | Datatype | Description |
|----|----------|-------------|
| `raw` | `neuro/meeg/mne/raw` | Resampled raw FIF file |

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `sfreq` | number | `250` | Target sampling frequency (Hz) |

### Advanced Options

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `npad` | string | `auto` | Padding length before FFT resampling |
| `window` | string | `boxcar` | Window function for resampling |
| `pad` | string | `reflect_limited` | Signal padding method |
| `events` | string | `None` | Event array to resample alongside data |
| `stim_picks` | string | `None` | Stim channel indices to resample with data |

## QC Outputs

- PSD before and after resampling (side-by-side comparison)
- HTML report (`out_report/report.html`)

## Container

`docker://brainlife/mne:1.0.2`

## Usage (VEPCON dataset)

Set `sfreq: 250` to downsample BioSemi Active Two data from 2048 Hz to 250 Hz.
