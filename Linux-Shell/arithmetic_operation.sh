#!/bin/bash
read eq
printf %.3f $(echo "$eq" |bc -l)
