{{/*
Expand the name of the chart.
*/}}
{{- define "template-server.openshift-repo" -}}
{{- printf "image-registry.openshift-image-registry.svc:5000/%s/agentk8s-tools:tpl-server"  .Release.Namespace | quote }}
{{- end }}

