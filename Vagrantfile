# vim: set ft=ruby:

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "public_network"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end
  # Ansible requires Python 2
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install python python-apt aptitude -y
  SHELL
end
