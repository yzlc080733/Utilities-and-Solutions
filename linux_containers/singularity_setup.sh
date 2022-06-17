# NOTICE: for ubuntu 20.04. see link REF below for other distributions

# FROM: https://docs.sylabs.io/guides/3.2/user-guide/installation.html#install-the-debian-ubuntu-package-using-apt
# REF: https://neuro.debian.net/pkgs/singularity-container.html

sudo wget -O- http://neuro.debian.net/lists/focal.gr.libre | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
sudo apt-key adv --recv-keys --keyserver hkps://keyserver.ubuntu.com 0xA5D32F012649A5A9

sudo apt-get update

sudo apt-get install singularity-container

echo "BASH FINISHED"
