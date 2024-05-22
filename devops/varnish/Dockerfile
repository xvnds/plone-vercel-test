# syntax=docker/dockerfile:1
FROM varnish:7.4

LABEL maintainer="Plone Foundation <collective@plone.org>" \
      org.label-schema.name="plone-vercel-test-varnish" \
      org.label-schema.description="plone-vercel-test Varnish image." \
      org.label-schema.vendor="Plone Foundation"

COPY etc/varnish.vcl /etc/varnish/default.vcl
