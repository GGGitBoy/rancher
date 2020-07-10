package client

const (
	ChangeMfaInputType         = "changeMfaInput"
	ChangeMfaInputFieldCaptcha = "captcha"
	ChangeMfaInputFieldSecret  = "secret"
)

type ChangeMfaInput struct {
	Captcha string `json:"captcha,omitempty" yaml:"captcha,omitempty"`
	Secret  string `json:"secret,omitempty" yaml:"secret,omitempty"`
}
