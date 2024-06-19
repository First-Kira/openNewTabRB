if RUBY_PLATFORM =~ /darwin/
  system("open -a Safari https://app.hackthebox.com")
else
  puts "This script is designed to run on macOS."
end
