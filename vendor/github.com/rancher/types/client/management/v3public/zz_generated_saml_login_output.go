package client

const (
	SamlLoginOutputType                = "samlLoginOutput"
	SamlLoginOutputFieldEnabledMfa     = "enabledMfa"
	SamlLoginOutputFieldIdpRedirectURL = "idpRedirectUrl"
)

type SamlLoginOutput struct {
	EnabledMfa     bool   `json:"enabledMfa,omitempty" yaml:"enabledMfa,omitempty"`
	IdpRedirectURL string `json:"idpRedirectUrl,omitempty" yaml:"idpRedirectUrl,omitempty"`
}
