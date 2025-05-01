# Instrumenting Django and Gunicorn with Splunk OpenTelemetry

Build and run the dockerized app using the following commands.
```
docker build --build-arg SPLUNK_REALM=<REALM> --build-arg SPLUNK_ACCESS_TOKEN=<TOKEN> -t django-docker .
docker run -p 8000:8000 django-docker
```

The build command expects a valid token and realm. The instrumentation is set up to also log at debug level and will also print spans to the console.

Open http://localhost:8000/hello to access the app.


Refer to `gunicorn.config.py` to see how tracing is setup.
