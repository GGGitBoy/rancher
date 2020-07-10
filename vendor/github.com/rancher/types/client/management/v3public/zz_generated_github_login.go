package client

const (
	GithubLoginType              = "githubLogin"
	GithubLoginFieldCaptcha      = "captcha"
	GithubLoginFieldCode         = "code"
	GithubLoginFieldDescription  = "description"
	GithubLoginFieldResponseType = "responseType"
	GithubLoginFieldTTLMillis    = "ttl"
)

type GithubLogin struct {
	Captcha      string `json:"captcha,omitempty" yaml:"captcha,omitempty"`
	Code         string `json:"code,omitempty" yaml:"code,omitempty"`
	Description  string `json:"description,omitempty" yaml:"description,omitempty"`
	ResponseType string `json:"responseType,omitempty" yaml:"responseType,omitempty"`
	TTLMillis    int64  `json:"ttl,omitempty" yaml:"ttl,omitempty"`
}
