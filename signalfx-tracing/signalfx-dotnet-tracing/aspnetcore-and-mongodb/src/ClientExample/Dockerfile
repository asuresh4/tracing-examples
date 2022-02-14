FROM mcr.microsoft.com/dotnet/core/sdk:3.1 as build

WORKDIR /build
COPY . .
RUN dotnet tool install -g Cake.Tool
ENV PATH="${PATH}:/root/.dotnet/tools"
RUN dotnet cake build.cake --runtime=linux-x64

FROM mcr.microsoft.com/dotnet/core/runtime:3.1

COPY --from=build /build/publish /app
WORKDIR /app

ADD https://github.com/signalfx/signalfx-dotnet-tracing/releases/download/v0.2.2/signalfx-dotnet-tracing_0.2.2_amd64.deb /tmp/sdt.deb
RUN dpkg -i /tmp/sdt.deb

RUN mkdir /var/log/signalfx

EXPOSE 5000

RUN dotnet --list-runtimes

ENV CORECLR_ENABLE_PROFILING 1
ENV CORECLR_PROFILER {B4C89B0F-9908-4F73-9F59-0D77C5A06874}
ENV CORECLR_PROFILER_PATH /opt/signalfx/SignalFx.Tracing.ClrProfiler.Native.so
ENV SIGNALFX_DOTNET_TRACER_HOME /opt/signalfx
ENV SIGNALFX_PROPAGATORS B3,W3C
ENV SIGNALFX_TRACE_LOG_DIRECTORY /var/log/signalfx
ENV SIGNALFX_SERVICE_NAME aspdotnet-swat-client
ENV SIGNALFX_TRACE_DEBUG true

ENTRYPOINT ["dotnet", "ClientExample.dll"]
