package client

const (
	DingtalkConfigType          = "dingtalkConfig"
	DingtalkConfigFieldProxyURL = "proxyUrl"
	DingtalkConfigFieldURL      = "url"
	DingtalkConfigFieldSecret    = "secret"
)

type DingtalkConfig struct {
	ProxyURL string `json:"proxyUrl,omitempty" yaml:"proxyUrl,omitempty"`
	URL      string `json:"url,omitempty" yaml:"url,omitempty"`
	Secret      string `json:"secret,omitempty" yaml:"secret,omitempty"`
}
