<h1 align="center">app-resample-raw-v2</h1>

<p align="center">
  Resamples raw MEG/EEG data to a new sampling frequency with MNE-Python and outputs the resampled raw file, before/after PSD plots and an HTML report.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.896"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.896-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Resamples raw MEG/EEG data to a new sampling frequency with MNE-Python and outputs the resampled raw file, before/after PSD plots and an HTML report.**

Loads a raw .fif file, calls raw.resample with the target sampling frequency and the padding/window options, and saves the result with a PSD comparison and a report. Use it to downsample high-rate EEG/MEG recordings (for example BioSemi data from 2048 Hz to 250 Hz) before further processing.

| | |
|---|---|
| **Inputs** | `neuro/meeg/mne/raw` |
| **Outputs** | `neuro/meeg/mne/raw` |
| **Container** | `brainlife/mne:1.0.2` |
| **Resources** | 1 CPUs · 16 GB memory · 1 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.896](https://doi.org/10.25663/brainlife.app.896) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `raw` | `neuro/meeg/mne/raw` | yes | Raw MEG/EEG recording (MNE .fif). |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/mne/raw` | Resampled raw data (raw.fif). |

<details>
<summary><b>Parameters</b> (6)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `sfreq` | number |  | New sample rate to use. |
| `npad` | string | `auto` | Padding before FFT resampling |
| `window` | string | `boxcar` | Resampling window type |
| `pad` | string | `reflect_limited` | Signal padding method |
| `events` | string | `None` | Event array to resample alongside data |
| `stim_picks` | string | `None` | Event array to resample alongside data |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.896](https://doi.org/10.25663/brainlife.app.896), choose `neuro/meeg/mne/raw` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/meeg/mne/raw`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/mne:1.0.2`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "mne": "/path/to/raw/mne",
       "sfreq": "",
       "npad": "auto",
       "window": "boxcar",
       "pad": "reflect_limited",
       "events": "None",
       "stim_picks": "None"
   }
   ```

3. Run `./main`.

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `sfreq` | number | `250` | Target sampling frequency (Hz) |

## Advanced Options

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

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- app-resample-raw-v2. brainlife.io App. [doi:10.25663/brainlife.app.896](https://doi.org/10.25663/brainlife.app.896)
- Gramfort A, et al. MEG and EEG data analysis with MNE-Python. Front Neurosci 7(267):1-13 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

Maintained by [@obVdo](https://github.com/obVdo).
