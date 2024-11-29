Vagrant.configure("2") do |config|
  config.vm.define "microservice1" do |microservice|
    microservice.vm.box = "ubuntu/focal64"
    microservice.vm.network "forwarded_port", guest: 5001, host: 5001
    microservice.vm.network "private_network", ip: "10.0.0.3"
    microservice.vm.synced_folder "./microservice1/", "/home/vagrant/microservice"
    microservice.vm.provision "shell", inline: <<-SHELL
        apt-get update
        apt-get install -y python3 python3-pip
        pip3 install flask flask-sqlalchemy
      SHELL
    microservice.vm.hostname = "microservice1"
  end

  config.vm.define "microservice2" do |microservice|
    microservice.vm.box = "ubuntu/focal64"
    microservice.vm.network "forwarded_port", guest: 5002, host: 5002
    microservice.vm.network "private_network", ip: "10.0.0.4"
    microservice.vm.synced_folder "./microservice2/", "/home/vagrant/microservice"
    microservice.vm.provision "shell", inline: <<-SHELL
        apt-get update
        apt-get install -y python3 python3-pip
        pip3 install flask flask-sqlalchemy
      SHELL
    microservice.vm.hostname = "microservice2"
  end

  config.vm.define "microservice3" do |microservice|
    microservice.vm.box = "ubuntu/focal64"
    microservice.vm.network "forwarded_port", guest: 5003, host: 5003
    microservice.vm.network "private_network", ip: "10.0.0.2"
    microservice.vm.synced_folder "./microservice3/", "/home/vagrant/microservice"
    microservice.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y python3 python3-pip
    pip3 install flask flask-sqlalchemy
  SHELL
  microservice.vm.hostname = "microservice3"
  end
end
