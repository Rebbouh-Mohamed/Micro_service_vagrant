Vagrant.configure("2") do |config|
  config.vm.define "microservice1" do |microservice|
    microservice.vm.box = "ubuntu/focal64"
    microservice.vm.network "forwarded_port", guest: 5001, host: 5001
    microservice.vm.synced_folder "./microservice1/", "/home/vagrant/microservice"
  end

  config.vm.define "microservice2" do |microservice|
    microservice.vm.box = "ubuntu/focal64"
    microservice.vm.network "forwarded_port", guest: 5002, host: 5002
    microservice.vm.synced_folder "./microservice2/", "/home/vagrant/microservice"
  end

  config.vm.define "microservice3" do |microservice|
    microservice.vm.box = "ubuntu/focal64"
    microservice.vm.network "forwarded_port", guest: 5003, host: 5003
    microservice.vm.synced_folder "./microservice3/", "/home/vagrant/microservice"
  end
end


#      microservice.vm.synced_folder "./microservice#{i}/", "/home/vagrant/microservice"