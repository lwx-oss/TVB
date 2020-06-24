#!/bin/bash


if [ -f "tvb.zip" ]; then
    rm "tvb.zip"
fi

zip -r -0 plugin.tvb.zip plugin.tvb.lwx
