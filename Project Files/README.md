# Flight Risk Deploy Package

This folder is the GitHub-ready version of the Flight Risk prototype.

## What to upload

Upload the entire contents of this folder to a new GitHub repository.

## How to make it publicly accessible

1. Create a GitHub repository.
2. Upload the files in this folder.
3. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
4. Connect your GitHub account and select the repository.
5. Set the main file path to `app.py`.
6. Deploy.

After deployment, Streamlit will give you a public link that anyone can click to use the app.

## Notes

- This package already includes a trained model in `artifacts/flight_risk_bundle.joblib`.
- The app uses historical flight options from the trained artifact, not live airline schedules.
- No large raw datasets are required for deployment.
