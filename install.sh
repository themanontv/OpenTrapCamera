#!/bin/bash

# Echo the license information

echo "OpenTrapCamera - open source wildlife trap camera that sends 
uploads to an S3 bucket. Copyright (C) 2025  Joseph Gadd

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"

# Install Packages
apt update && xargs -a packages.txt sudo apt install

# Create the config file
read -sp "AWS Access Key: " access_key
read -sp "AWS Secret Key: " secret_key
read -sp "Bucket Name: " bucket_name

echo -e "[AWS]\naccess_key = ${access_key}\nsecret_key = ${secret_key}\nbucket_name = ${bucket_name}" > config