# Customer Retention Dashboard on Streamlit

This app hosts the **original interactive HTML/CSS/JavaScript dashboard** inside
Streamlit. It retains the Overview, Model Results and Dataset tabs, filters and
data already embedded in `dashboard.html`.

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push the **contents of this folder** to a GitHub repository you own.
2. Sign into https://share.streamlit.io/ with that GitHub account.
3. Create an app from the repository and set the main file to `app.py`.
4. Choose an available public subdomain ending in `.streamlit.app`.

The project contains no database credentials or private API keys. Its data is
already embedded in the supplied HTML. The web page is displayed inside an
iframe because Streamlit does not natively execute an arbitrary full HTML app
as its main document. On mobile, the embedded page may scroll independently.
