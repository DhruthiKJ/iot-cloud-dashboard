\# IoT Simulated Cloud Pipeline



A simulated IoT-to-cloud pipeline built from scratch — no physical hardware required. This project simulates sensor devices, streams their data to a backend over HTTP, stores it in a cloud database, and visualizes it on a live dashboard.



Built after realizing a "hands-on" IoT bootcamp wasn't actually hands-on — this is what I built instead to genuinely learn how device-to-cloud pipelines work.



\## What it does



\- Simulates multiple sensor readings (temperature, humidity) on a timer, mimicking real IoT devices

\- Sends readings to a backend server over HTTP (POST requests)

\- Server stores every reading in a Supabase (Postgres) cloud database

\- A live Streamlit dashboard reads from the database and displays real-time charts and metrics



\## Architecture



```

sensor.py  --(HTTP POST)-->  server.py (Flask)  --(insert)-->  Supabase (Postgres)

&#x20;                                                                       |

&#x20;                                                             dashboard.py (Streamlit) <--(read)

```



\- \*\*`sensor.py`\*\* — simulates a device generating readings and sending them via HTTP

\- \*\*`server.py`\*\* — Flask server that receives readings and writes them to Supabase

\- \*\*`dashboard.py`\*\* — Streamlit app that queries Supabase and renders live charts



\## Tech stack



\- Python

\- Flask (backend API)

\- Supabase (cloud Postgres database)

\- Streamlit (dashboard/frontend)

\- `requests`, `python-dotenv`



\## Running it locally



1\. Clone the repo and install dependencies:

&#x20;  ```

&#x20;  pip install flask requests supabase streamlit python-dotenv

&#x20;  ```

2\. Create a `.env` file in the project root with:

&#x20;  ```

&#x20;  SUPABASE\_URL=your\_supabase\_project\_url

&#x20;  SUPABASE\_KEY=your\_supabase\_key

&#x20;  ```

3\. Set up a `sensor\_readings` table in Supabase with columns: `temperature`, `humidity`, `timestamp`.

4\. Run all three components, each in its own terminal:

&#x20;  ```

&#x20;  python server.py

&#x20;  python sensor.py

&#x20;  python -m streamlit run dashboard.py

&#x20;  ```



\## What I learned



\- How HTTP request/response communication works between a client and a server

\- Building a REST endpoint with Flask

\- Connecting to and writing data into a cloud database (Supabase/Postgres)

\- Row Level Security (RLS) policies and why they matter

\- Keeping secrets out of source control with `.env` and `.gitignore`

\- Building a real-time dashboard with Streamlit



\## Possible next steps



\- Swap HTTP for MQTT to reflect how real IoT devices typically communicate

\- Add simple anomaly detection on incoming readings

\- Deploy the server to a cloud host so it's reachable outside localhost

