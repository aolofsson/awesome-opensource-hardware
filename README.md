# awesome-opensource-hardware

A curated list of awesome open source hardware tools.

* Categorized
* Alphabetical (per category)
* Requirements
    * link should be to source code repository
	* open source projects only
	* working projects only (not WIP/rusty)
* One tag line sentence per project.

## Accelerators

* [aes](https://github.com/secworks/aes)
  * Symmetric block cipher AES (Advanced Encryption Standard)
* [ara](https://github.com/pulp-platform/ara)
  * Vector Unit, compatible with the RISC-V Vector Extension
* [BISMO](https://github.com/EECS-NTNU/bismo/)
  * Chisel-based bit-serial matrix multiplication accelerator generator
* [FINN](https://github.com/Xilinx/finn)
  * Quantized NN to FPGA dataflow accelerator generator
* [FFTGenerator](https://github.com/ucb-bar/FFTGenerator)
  * MMIO-Based FFT Generator
* [fpu](https://github.com/dawsonjon/fpu)
  * Synthesizable ieee 754 floating point library in verilog
* [garnet](https://github.com/StanfordAHA/garnet)
  * CGRA generator
* [gemmini](https://github.com/ucb-bar/gemmini)
  * Berkeley Spatial Array Generator
* [gplgpu](https://github.com/asicguy/gplgpu)
  * GPL v3 2D/3D graphics engine in verilog
* [core_jpeg](https://github.com/ultraembedded/core_jpeg)
  * High throughput JPEG decoder in Verilog for FPGA
* [fftgenerator](https://github.com/ucb-bar/FFTGenerator)
  * Chisel based FFT generator
* [h265-encoder-rtl](https://github.com/openasic-org/h265-encoder-rtl)
  * H.265 Video Encoder IP Core
* [LogicNets](https://github.com/Xilinx/logicnets)
  * Train and generate LUT-based neural networks
* [nvdla](https://github.com/nvdla/hw)
  * NVIDIA Deep Learning Accelerator (NVDLA)
* [NyuziProcessor](https://github.com/jbush001/NyuziProcessor)
  * GPGPU microprocessor architecture
* [openofdm](https://github.com/jhshi/openofdm)
  * 802.11 OFDM PHY decoder
* [sha3](https://github.com/ucb-bar/sha3)
  * Berkeley SHAR3 ROCC Accelerator
* [spiral](https://github.com/spiral-software/spiral-software)
  * Spiral based FFT generator
* [tvm-vta](https://github.com/apache/tvm-vta)
  * Opwn, modular, deep learning accelerator
* [VeriGOOD-ML](https://github.com/VeriGOOD-ML/public)
  * Verilog Generator, Optimized for Designs for Machine Learning
* [VeriGPU](https://github.com/hughperkins/VeriGPU)
  * OpenSource GPU, loosely based on RISC-V ISA
* [verilog-lfsr](https://github.com/alexforencich/verilog-lfsr)
  * Parametrizable combinatorial parallel LFSR/CRC module
* [vortex](https://github.com/vortexgpgpu/vortex)
  * Full-system RISCV-based GPGPU processor

## Analog

* [AMS_KGD](https://github.com/USCPOSH/AMS_KGD)
  * Repository for Known Good Analog Designs (KGDs)
* [open-pmic](https://github.com/westonb/open-pmic)
  * Current mode buck converter on the SKY130 PDK
* [Analog Basic Blocks/LDO](https://github.com/mabrains/Analog_blocks)
  * Repo that has designs with the following: OTA, BandGap and LDO design on Skywaters 130nm.

## Boards

* [parallella-hw](https://github.com/parallella/parallella-hw)
  * Parallella board design files

## Connectivity

* [aib](https://github.com/chipsalliance/aib-phy-hardware)
  * Advanced Interface Bus (AIB) die to die hardware
* [aib-protocols](https://github.com/chipsalliance/aib-protocols)
  * Advanced Interface Bus (AIB) Protocol IP
* [axi](https://github.com/pulp-platform/axi)
  * AXI SystemVerilog synthesizable IP
* [axi4_aib_bridge](https://github.com/lmco/axi4_aib_bridge)
  * AXI4/AIB Bridge RTL
* [core_ddr3_controller](https://github.com/ultraembedded/core_ddr3_controller)
  * DDR3 memory controller in Verilog for various FPGAs
* [hdmi](https://github.com/hdl-util/hdmi)
  * Send video/audio over HDMI on an FPGA
* [i2c](https://github.com/hdl-util/i2c)
  * Fully featured implementation of Inter-IC (I2C) bus master
* [litedram](https://github.com/enjoy-digital/litedram)
  * Small footprint and configurable DRAM (litex)
* [liteeth](https://github.com/enjoy-digital/liteeth)
  * Small footprint and configurable Ethernet core
* [litescope](https://github.com/enjoy-digital/litescope)
  * Small footprint and configurable embedded FPGA logic analyzer
* [litepice](https://github.com/enjoy-digital/litepcie)
  * Small footprint and configurable PCIe core
* [OpenSERDES](https://github.com/SparcLab/OpenSERDES)
  * Digitally synthesizable architecture for SerDes using Skywater130
* [pymtl3-net](https://github.com/cornell-brg/pymtl3-net)
  * Cornell parameterizable OCN (on-chip network) generator
* [ravenoc](https://github.com/aignacio/ravenoc)
  * Configurable HDL NoC (Network-On-Chip)
* [tnoc](https://github.com/taichi-ishitani/tnoc)
  * Network on Chip Implementation written in SytemVerilog
* [verilog-axis](https://github.com/alexforencich/verilog-axis)
  * Verilog AXI stream components for FPGA implementation
* [verilog-ethernet](https://github.com/alexforencich/verilog-ethernet)
  * Verilog Ethernet components for FPGA implementation
* [verilog-i2c](https://github.com/alexforencich/verilog-i2c)
  * Verilog I2C interface for FPGA implementation
* [verilog-uart](https://github.com/alexforencich/verilog-uart)
  * Verilog UART
* [verilog-pcie](https://github.com/alexforencich/verilog-pcie)
  * Verilog PCI express components
* [verilog-wishbone](https://github.com/alexforencich/verilog-wishbone)
  * Verilog wishbone components
* [wav-d2d-hw](https://github.com/waviousllc/wav-d2d-hw)
  * 8lane Wlink with D2D and a single AXI Target/Initiator
* [wav-lpddr-hw](https://github.com/waviousllc/wav-lpddr-hw)
  * DDR (WDDR) Physical interface (PHY) Hardware
* [wav-slink-hw](https://github.com/waviousllc/wav-slink-hw)
  * Chiplet link
* [wav-wlink-hw](https://github.com/waviousllc/wav-wlink-hw)
  * Chiplet link

## CPU cores

* [a2i](https://github.com/openpower-cores/a2i)
  * A2I POWER processor core RTL (VHDL)
* [black-parrot](https://github.com/black-parrot/black-parrot)
  * Linux-capable RISC-V multicore
* [Cores-SweRV](https://github.com/chipsalliance/Cores-SweRV)
  * SweRV EH1 RISC-Vcore
* [Cores-SweRV-EL2](https://github.com/chipsalliance/Cores-SweRV-EL2)
  * SweRV EL2 RISC-V Core
* [core-v-verif](https://github.com/openhwgroup/core-v-verif)
  * Functional verification project for the CORE-V family of RISC-V cores
* [cva6](https://github.com/openhwgroup/cva6)
  * Linux capable RISC-V CPU
* [cv32e40p](https://github.com/openhwgroup/cv32e40p)
  * RV32IMFCX RISC-V 4-stage RISC-V CPU
* [ibex](https://github.com/lowRISC/ibex)
  * Small 32 bit RISC-V CPU core

* [microwatt](https://github.com/antonblanchard/microwatt)
  * Open POWER ISA softcore written in VHDL 2008
* [neorv32](https://github.com/stnolting/neorv32)
  * Customizable and highly extensible MCU-class 32-bit RISC-V (VHDL)
* [OpenXiangShan](https://github.com/OpenXiangShan/XiangShan)
  * Open-source high-performance RISC-V processor
* [picorv32](https://github.com/YosysHQ/picorv32)
  * Size-Optimized RISC-V CPU
* [rocket-chip](https://github.com/chipsalliance/rocket-chip)
  * Linux capable RISC-V Rocket Chip Generator
* [serv](https://github.com/olofk/serv)
  * SErial RISC-V CPU
* [snitch](https://github.com/pulp-platform/snitch)
  * Lean but mean RISC-V system

## FPGAs

* [FABulous](https://github.com/FPGA-Research-Manchester/FABulous)
  * Fabric generator and CAD tools
* [fabric_team](https://github.com/ucb-cs250/fabric_team)
  * ucb-cs250 FPGA class project
* [OpenFPGA](https://github.com/lnis-uofu/OpenFPGA)
  * FPGA IP Generator
* [prga](https://github.com/PrincetonUniversity/prga)
  * Open-source FPGA research and prototyping framework

## Libraries

* [basic_verilog](https://github.com/pConst/basic_verilog)
  * Library of SystemVerilog components
* [common_cells](https://github.com/pulp-platform/common_cells)
  * Library of SystemVerilog components
* [hdl](https://github.com/analogdevicesinc/hdl)
  * Library of Analog Deveices specific components
* [oh](https://github.com/aolofsson/oh)
  * Library of Verilog components
* [basejump_stl](https://github.com/bespoke-silicon-group/basejump_stl)
  * Library of SystemVerilog components


## Memory
* [core_axi_cache](https://github.com/ultraembedded/core_axi_cache)
  * 128KB AXI cache (32-bit in, 256-bit out)
* [HuanCun](https://github.com/OpenXiangShan/HuanCun)
  * Open-source high-performance non-blocking cache
* [openram](https://github.com/VLSIDA/OpenRAM)
  * Static random access memory (SRAM) compiler.
* [lake](https://github.com/StanfordAHA/lake)
  * Synthesizable memory generator

## Packaging

* [bsg_packaging](https://github.com/bespoke-silicon-group/bsg_packaging)
  * Open-Source Hardware Accelerator Packages and Sockets

## Retro

* [VerilogBoy](https://github.com/zephray/VerilogBoy)
  * Game Boy compatible machine with Verilog

## Systems

* [Beagle_SDR_GPS](https://github.com/jks-prv/Beagle_SDR_GPS)
  * KiwiSDR: BeagleBone web-accessible GPS/SDR
* [bsg_manycore](https://github.com/bespoke-silicon-group/bsg_manycore)
  * Tile based architecture designed for computing efficiency, scalability
* [cep](https://github.com/mit-ll/CEP)
  * RISC-V based Common Evaluation Platform (CEP)
* [esp](https://github.com/sld-columbia/esp)
  * Heterogeneous SoC architecture and IP design platform
* [hero](https://github.com/pulp-platform/hero)
  * FPGA-based research platform for heterogeneous design
* [litex](https://github.com/enjoy-digital/litex)
  * SoC builder framework
* [openFASOC](https://github.com/idea-fasoc/OpenFASOC)
  * Open Source FASOC generators
* [openpiton](https://github.com/PrincetonUniversity/openpiton)
  * General purpose, multithreaded manycore processor
* [opentitan](https://github.com/lowRISC/opentitan)
  * Open source silicon root of trust
* [openwifi-hw](https://github.com/open-sdr/openwifi-hw)
  * IEEE 802.11 WiFi baseband FPGA (chip) design
* [pulp](https://github.com/pulp-platform/pulp)
  * Multicore RISC-V based SoC
* [pulpissimo](https://github.com/pulp-platform/pulpissimo)
  * Single core RISC-V based SoC
