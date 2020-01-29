#!/bin/sh

echo "------------------------- Project Setup -------------------------------"

export UAS_ROOT=$PWD
export UAS_BUILD=$UAS_ROOT/work
export SCALE_SW=$UAS_ROOT/external/scale-sw
export SCALE_HW=$UAS_ROOT/external/scale-hw

if [ -z $UAS_ARM_TOOLCHAIN_ROOT ] ; then
    export UAS_ARM_TOOLCHAIN_ROOT=/usr/bin/
fi

if [ -z $IAMCU_TOOLCHAIN_DIR ] ; then
    export IAMCU_TOOLCHAIN_DIR=
fi

if [ -z $VIVADO_ROOT ] ; then
    export VIVADO_ROOT=$XILINX_VIVADO
fi

if [ -z $UAS_MICROBLAZE_TOOLCHAIN_ROOT ] ; then
    export UAS_MICROBLAZE_TOOLCHAIN_ROOT=/opt/Xilinx/SDK/2019.1/gnu/microblaze/lin/bin
fi

if [ -z $OPENOCD ] ; then
    export OPENOCD=openocd
fi

mkdir -p $UAS_BUILD

echo "UAS_ROOT  = $UAS_ROOT"
echo "UAS_BUILD = $UAS_BUILD"
echo "SCALE_SW  = $SCALE_SW"
echo "SCALE_HW  = $SCALE_HW"
echo "OPENOCD   = $OPENOCD"
echo "---"
echo "UAS_ARM_TOOLCHAIN_ROOT        = $UAS_ARM_TOOLCHAIN_ROOT"
echo "UAS_MICROBLAZE_TOOLCHAIN_ROOT = $UAS_MICROBLAZE_TOOLCHAIN_ROOT"
echo "IAMCU_TOOLCHAIN_DIR           = $IAMCU_TOOLCHAIN_DIR"
echo "VIVADO_ROOT                   = $VIVADO_ROOT"
echo "-----------------------------------------------------------------------"
