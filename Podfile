# Uncomment the next line to define a global platform for your project
# platform :ios, '9.0'

target 'TranslatorApp' do
  # Comment the next line if you don't want to use dynamic frameworks
  use_frameworks!

  # Pods for TranslatorApp
  pod 'GoogleMLKit/Translate', '3.2.0'

end


post_install do |installer|
  installer.pods_project.build_configurations.each do |config|
    config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = '14.0'
    config.build_settings["EXCLUDED_ARCHS[sdk=iphonesimulator*]"] = "arm64"
  end
end