#!/bin/sh
macro () {
pwd > /tmp/missing/pwdinmacro.txt
}
polo () {
cd $(</tmp/missing/pwdinmacro.txt)
}
