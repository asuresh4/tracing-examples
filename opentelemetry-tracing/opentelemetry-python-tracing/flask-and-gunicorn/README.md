Run the following commands to start a dockerized app.

```
docker build --build-arg SPLUNK_REALM=REALM --build-arg SPLUNK_ACCESS_TOKEN=TOKEN -t flask-hello-new .
docker run  -p 8000:8000 flask-hello-new
```

Access `http://localhost:8000/hello/` to generate logs and traces.

Example logs from the application.

```
[2025-05-30 20:14:55 +0000] [1] [INFO] Starting gunicorn 23.0.0
[2025-05-30 20:14:55 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
[2025-05-30 20:14:55 +0000] [1] [INFO] Using worker: gthread
[2025-05-30 20:14:55 +0000] [29] [INFO] Booting worker with pid: 29
[2025-05-30 20:14:55 +0000] [66] [INFO] Booting worker with pid: 66
[2025-05-30 20:14:55 +0000] [103] [INFO] Booting worker with pid: 103
[2025-05-30 20:14:55 +0000] [140] [INFO] Booting worker with pid: 140
test info log
2025-05-30 20:14:56,001 INFO [app] [app.py:17] [trace_id=68d148234df9a0d2772a32aa852bff37 span_id=6037f8922c857494 resource.service.name=swat-9358 trace_sampled=True] - test info log
test warning log
2025-05-30 20:14:56,002 WARNING [app] [app.py:18] [trace_id=68d148234df9a0d2772a32aa852bff37 span_id=6037f8922c857494 resource.service.name=swat-9358 trace_sampled=True] - test warning log
test error log
2025-05-30 20:14:56,002 ERROR [app] [app.py:19] [trace_id=68d148234df9a0d2772a32aa852bff37 span_id=6037f8922c857494 resource.service.name=swat-9358 trace_sampled=True] - test error log
```

