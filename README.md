# app-resample-raw-v2

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Resamples raw MEG/EEG data to a new sampling frequency with MNE-Python and outputs the resampled raw file, before/after PSD plots and an HTML report.**

Loads a raw .fif file, calls raw.resample with the target sampling frequency and the padding/window options, and saves the result with a PSD comparison and a report. Use it to downsample high-rate EEG/MEG recordings (for example BioSemi data from 2048 Hz to 250 Hz) before further processing.

| | |
|---|---|
| 📥 **Inputs** | `neuro/meeg/mne/raw` |
| 📤 **Outputs** | `neuro/meeg/mne/raw` |
| 🐳 **Container** | `brainlife/mne:1.0.2` |
| ⚙️ **Resources** | 1 CPUs · 16 GB memory · 1 h walltime |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.896](https://doi.org/10.25663/brainlife.app.896) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `raw` | `neuro/meeg/mne/raw` | yes | Raw MEG/EEG recording (MNE .fif). |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/mne/raw` | Resampled raw data (raw.fif). |

<details>
<summary><b>⚙️ Parameters</b> (6)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `sfreq` | number |  | New sample rate to use. |
| `npad` | string | `auto` | Padding before FFT resampling |
| `window` | string | `boxcar` | Resampling window type |
| `pad` | string | `reflect_limited` | Signal padding method |
| `events` | string | `None` | Event array to resample alongside data |
| `stim_picks` | string | `None` | Event array to resample alongside data |

</details>

📚 **References used by this App:**
- Gramfort A, et al. MEG and EEG data analysis with MNE-Python. Front Neurosci 7(267):1-13 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)

<!-- brainlife-app:end -->

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
