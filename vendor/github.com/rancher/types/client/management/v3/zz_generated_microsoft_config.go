package client

const (
	MicrosoftConfigType          = "microsoftConfig"
	MicrosoftConfigFieldProxyURL = "proxyUrl"
	MicrosoftConfigFieldURL      = "url"
)

type MicrosoftConfig struct {
	ProxyURL string `json:"proxyUrl,omitempty" yaml:"proxyUrl,omitempty"`
	URL      string `json:"url,omitempty" yaml:"url,omitempty"`
}
