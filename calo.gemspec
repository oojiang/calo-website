# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "calo"
  spec.version       = "0.1.0"
  spec.authors       = ["Oliver Jiang"]
  spec.email         = ["ojiang@berkeley.edu"]

  spec.summary       = "jekyll theme for cal origami's website"
  spec.homepage      = "https://calorigami.berkeley.edu/"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_data|_layouts|_includes|_sass|LICENSE|README|_config\.yml)!i) }

  spec.add_runtime_dependency "jekyll", "~> 4.3"
end
