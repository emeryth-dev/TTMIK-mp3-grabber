#!/bin/bash

while read line; do wget $line; done < full_list.txt

