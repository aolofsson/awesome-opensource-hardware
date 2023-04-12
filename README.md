# awesome-opensource-hardware

A curated list of awesome open source hardware tools, generators, and reusable designs.

* Categorized
* Alphabetical (per category)
* Requirements
    * link should be to source code repository
	* open source projects only
	* working projects only (not WIP/rusty)
* One tag line sentence per project.

# Table of Contents

## Compilers
  * [Build Systems](#build-systems)
  * [Digital](#digital-compilers)
  * [FPGA](#fpga-compilers)
  * [Layout](#layout-compilers)

## Design Tools
  * [Analog](#analog-design)
  * [Board](#board-design)
  * [Chip Layout](#chip-layout)
  * [Digital](#digital-design)
  * [Documentation](#documentation)
  * [FPGA](#fpga-design)
  * [Registers](#register-design)

## Verification
  * [Analog](#analog-verification)
  * [Benchmarks](#benchmarks)
  * [Digital](#digital-verification)
  * [Waveform Viewers](#waveform-viewers)

## Designs & Generators
  * [Accelerators](#accelerators)
  * [Analog Circuits](#analog-circuits)
  * [Chip Packages](#chip-packages)
  * [Boards](#board-designs)
  * [Connectivity](#connectivity)
  * [CPUs](#cpus)
  * [FPGA Architectures](#fpga-architectures)
  * [Libraries](#libraries)
  * [Memory](#memory)
  * [Systems](#systems)

# Compilers

## Build Systems
* [bazelhdl](https://github.com/hdl/bazel_rules_hdl)
  * Bazel based hdl build system
* [bender](https://github.com/pulp-platform/bender)
  * Dependency management tool for hardware projects.
* [chipyard](https://github.com/ucb-bar/chipyard)
  * Agile RISC-V SoC Design Framework.
* [cocoon](https://github.com/pku-dasys/cocoon)
  * An infrastructure for integrated EDA
* [edalize](https://github.com/olofk/edalize)
  * An abstraction library for interfacing EDA tools.
* [fusesoc](https://github.com/olofk/fusesoc)
  * Package manager and build abstraction tool for FPGA/ASIC development.
* [hammer](https://github.com/ucb-bar/hammer)
  * Agile physical design component part of UC Berkeley Chipyard framework.
* [hwtBuildsystem](https://github.com/Nic30/hwtBuildsystem)
  * Library of utils for interaction with the vendor tools.
* [legoHDL](https://github.com/c-rus/legoHDL)
  * Command line HDL package manager and development tool.
* [mflowgen](https://github.com/mflowgen/mflowgen)
  * Build-system generator for ASIC and FPGA design-space exploration.
* [siliconcompiler](https://github.com/siliconcompiler/siliconcompiler)
  * Build system that automates translation from source code to silicon.

## Digital Compilers
* [abc](https://github.com/berkeley-abc/abc)
  * System for sequential logic synthesis and formal verification
* [act](https://github.com/asyncvlsi/act)
  * Asynchronous circuit compiler tools
* [amaranth](https://github.com/amaranth-lang/amaranth)
  * Python based hardware design framework
* [bsc](https://github.com/B-Lang-org/bsc)
  * Compiler, simulator, and tools for the Bluespec Hardware Description Language
* [calyx](https://github.com/cucapra/calyx)
  * Intermediate language and infrastructure compilers that generate custom hardware accelerators
* [chisel](https://github.com/chipsalliance/chisel3)
  * Scala based hardware description language
* [circt](https://github.com/llvm/circt)
  * Circuit IR Compilers and Tools
* [clash](https://github.com/clash-lang/clash-compiler)
  * Haskell to VHDL/Verilog/SystemVerilog compiler
* [cocotbext-axi](https://github.com/alexforencich/cocotbext-axi)
  * AXI interface modules for Cocotb
* [cocotbext-pcie](https://github.com/alexforencich/cocotbext-pcie)
  * PCI express simulation framework for Cocotb
* [coreir](https://github.com/rdaly525/coreir)
  * LLVM-style hardware compiler with first class support for generators
* [dfiant](https://github.com/DFiantHDL/DFiant)
  * Dataflow Hardware Description Language
* [Fault](https://github.com/AUCOHL/Fault)
  * Design-for-testing (DFT) Solution
* [firrtl](https://github.com/chipsalliance/firrtl)
  * Intermediate Representation for RTL
* [gamma](https://github.com/maestro-project/gamma)
  * Optimizes mapping of DNN models on DNN Accelerators
* [halide](https://github.com/halide/Halide)
  * Language for fast, portable data-parallel computation
* [halide-to-hardware](https://github.com/StanfordAHA/Halide-to-Hardware)
  * Hardware generator combining halide and coreir
* [hdlconvertor](https://github.com/Nic30/hdlConvertor)
  * Verilog/VHDL parser preprocessor and code generator for C++/Python based on ANTL4
* [hs-to-coq](https://github.com/plclub/hs-to-coq)
  * Convert Haskell source code to Coq source code
* [livehd](https://github.com/masc-ucsc/livehd)
  * Infrastructure for live interactive synthesis and simulation
* [llhd](https://github.com/fabianschuiki/llhd)
  * Intermediate representation for digital circuit descriptions
* [lsoracle](https://github.com/lnis-uofu/LSOracle)
  * Famework built on EPFL logic synthesis libraries.
* [lstools](https://github.com/lsils/lstools-showcase)
  * Showcase examples for EPFL logic synthesis libraries
* [kami](https://github.com/mit-plv/kami)
  * Platform for High-Level Parametric Hardware Specification and its Modular Verification
* [magma](https://github.com/phanrahan/magma/)
  * Python based hardware design language
* [matchlib](https://github.com/NVlabs/matchlib)
  * Synthesizable SystemC/C++ library of commonly-used hardware functions
* [matchclib_connections](https://github.com/hlslibs/matchlib_connections)
  * Synthesizable SystemC library implementing latency-insensitive channels
* [mockturtle](https://github.com/lsils/mockturtle)
  * C++ logic network library
* [myhdl](https://github.com/myhdl/myhdl)
  * Python based hardware description and verification language
* [naja](https://github.com/xtofalex/naja)
  * Structural Netlist API (and more) for EDA post synthesis flow development
* [netlist-paths](https://github.com/jameshanlon/netlist-paths)
  * A library and command-line tool for querying a Verilog netlist
* [panda-bambu](https://github.com/ferrandi/PandA-bambu)
  * High level synthesis (HLS) C/C++ framework
* [pipelinec](https://github.com/JulianKemmerer/PipelineC)
  * C-like hardware description language (HDL) with automatic pipelining
* [pygears](https://github.com/bogdanvuk/pygears)
  * Python based hardware design framework
* [pymtl3](https://github.com/pymtl/pymtl3)
  * Python hardware generation, simulation, and verification framework
* [pyrtl](https://github.com/UCSBarchlab/PyRTL)
  * Python integrated design and simulation framework
* [pysysc](https://github.com/accellera-official/PySysC)
  * Python package to make SystemC usable from Python
* [pyverilog](https://github.com/PyHDI/Pyverilog)
  * Python design toolkit for Verilog HDL
* [rohd](https://github.com/intel/rohd)
  * Dart based framework for describing and verifying hardware
* [sandpiper-saas](https://gitlab.com/rweda/sandpiper-saas)
  * A CLI to Redwood EDA, LLC's free SandPiper™ TL-Verilog compiler microservice
* [silice](https://github.com/sylefeb/Silice)
  * Language that simplifies prototyping and writing algorithms on FPGA architectures
* [skidl](https://github.com/devbisme/skidl)
  * SKiDL is a module that extends Python with the ability to design electronic circuits
* [slang](https://github.com/MikePopoloski/slang)
  * Library for lexing, parsing, type checking, and elaborating SystemVerilog code
* [sodaopt](https://gitlab.pnnl.gov/sodalite/soda-opt)
  * Optimizer leveraging mlir to extract, optimize, translate HLSinto LLVM IR
* [spinalhdl](https://github.com/SpinalHDL/SpinalHDL)
  * Scala based HDL
* [spydrnet](https://github.com/byuccl/spydrnet)
  * Framework for analyzing and transforming Verilog netlists
* [surelog](https://github.com/chipsalliance/Surelog)
  * SystemVerilog IEEE 2017 Pre-processor, Parser, Elaborator, UHDM Compiler
* [sv-parser](https://github.com/dalance/sv-parser)
  * SystemVerilog IEEE 1800-2017 parser library
* [sv2v](https://github.com/zachjs/sv2v)
  * SystemVerilog to Verilog conversion
* [systemc](https://github.com/accellera-official/systemc)
  * SystemC system design and verification language that spans hardware and software
* [systemc-compiler](https://github.com/intel/systemc-compiler)
  * Translates synthesizable SystemC to synthesizable Verilog
* [uhdm](https://github.com/chipsalliance/UHDM)
  * Universal object model for IEEE SystemVerilog designs
* [verible](https://github.com/chipsalliance/verible)
  * Suite of SystemVerilog developer tools, including a parser, style-linter, and formatter
* [veriloggen](https://github.com/PyHDI/veriloggen)
  * Mixed-Paradigm Hardware Construction Framework
* [verik](https://github.com/frwang96/verik)
  * Kotlin based hardware description language
* [Vlsir](https://github.com/Vlsir/Vlsir)
  * Interchange formats for chip design
* [xls](https://github.com/google/xls)
  * Google framework for hardware synthesis
* [yosys](https://github.com/YosysHQ/yosys)
  * Yosys Open SYnthesis Suite

## FPGA Compilers
* [amf-placer](https://github.com/zslwyuan/AMF-Placer)
  * Timing-driven analytical mixed-size FPGA placer
* [dreamplacefpga](https://github.com/rachelselinar/DREAMPlaceFPGA)
  * Analytical Placer for Large Scale Heterogeneous FPGA
* [flowtune](https://github.com/Yu-Utah/FlowTune)
  * FPGA synehsis and PNR optimizer
* [nextpnr](https://github.com/YosysHQ/nextpnr)
  * FPGA place and route tool
* [vtr](https://github.com/verilog-to-routing/vtr-verilog-to-routing)
  * FPGA place and route tool

## Layout Compilers
* [align](https://github.com/ALIGN-analoglayout/ALIGN-public)
  * Automatic layout generator for analog circuits
* [bag](https://github.com/ucb-art/BAG_framework)
  * Berkeley analog layout generator
* [bigspicy](https://github.com/google/bigspicy)
  * Tool for merging circuit descriptions
* [dreamplace](https://github.com/limbo018/DREAMPlace)
  * Deep learning toolkit-enabled VLSI placement
* [Layout21](https://github.com/dan-fritchman/Layout21)
  * Integrated Circuit Layout
* [magical](https://github.com/magical-eda/MAGICAL)
  * Machine Generated Analog IC Layout
* [openroad](https://github.com/The-OpenROAD-Project/OpenROAD)
  * Complete RTL2GDS platform

# Design Tools

## Analog Design
* [OpenPLC_Editor](https://github.com/thiagoralves/OpenPLC_Editor)
  * IDE capable of creating programs for the OpenPLC Runtime
* [oregano](https://github.com/drahnr/oregano)
  * Schematic capture and circuit simulator
* [qucs_s](https://github.com/ra3xdh/qucs_s)
  * Integrated circuit simulator with Graphical User Interface
* [xschem](https://github.com/StefanSchippers/xschem)
  * Schematic editor for VLSI/Asic/Analog custom designs

## Board Design
* [boardview](https://github.com/whitequark/kicad-boardview)
  * Reads KiCAD PCB layout files and writes ASCII Boardview files
* [cuflow](https://github.com/jamesbowman/cuflow)
  * Experimental procedural PCB layout program
* [datasheet-scrubber](https://github.com/idea-fasoc/datasheet-scrubber)
  * Utility that scrubs PDF datasheets/documents in order to extract key circuit information
* [freecad](https://github.com/FreeCAD/FreeCAD)
  * 3D parametric CAD for building models of components for KiCad 3D preview (also enclosures)
* [kicad](https://github.com/KiCad/kicad-source-mirror)
  * Board design framework
* [pcbflow](https://github.com/michaelgale/pcbflow)
  * Python based Printed Circuit Board (PCB) layout and design package based on CuFlow

## Chip Layout
* [chip_art](https://github.com/jazvw/chip_art)
  * Convert an image to a GDS format for inclusion in a zerotoasic project
* [coriolis](https://gitlab.lip6.fr/vlsi-eda/coriolis.git)
  * RTL2GDS toolchain for mature nodes
* [gds3d](https://github.com/trilomix/GDS3D)
  * Reads GDSII layout and renders in 3D.
* [gdsfactory](https://github.com/gdsfactory/gdsfactory)
  * Python package to generate GDS layouts.
* [gdstk](https://github.com/heitzmann/gdstk)
  * C++/Python library for creation and manipulation of GDSII and OASIS files.
* [gdspy](https://github.com/heitzmann/gdspy)
  * Python module for creating GDSII stream files, usually CAD layouts.
* [klayout](https://github.com/KLayout/klayout)
  * Layout viewer
* [lclayout](https://codeberg.org/librecell/lclayout)
  * Layout generator for CMOS standard-cells
* [netgen](https://github.com/RTimothyEdwards/netgen)
  * LVS tool for comparing SPICE or verilog netlists
* [phidl](https://github.com/amccaugh/phidl)
  * Python GDS layout and CAD geometry creation
* [probe3.0](https://github.com/ABKGroup/PROBE3.0)
  * Process/design DTCO path finding technology

## Digital Design
* [circuitgraph](https://github.com/circuitgraph/circuitgraph)
  * Tools for working with circuits as graphs in python
* [makerchip-app](https://gitlab.com/rweda/makerchip-app)
  * Launches Makerchip.com as a virtual desktop application
* [verilog-mode](https://www.veripool.org/verilog-mode/)
  * Popular free Verilog mode for Emacs

## Documentation
* [graphviz](https://github.com/xflr6/graphviz)
  * Python library for graph cration and rendering in DOT language
* [memory-layout-diagram](https://github.com/gerph/memory-layout-diagram)
  * Diagrams for memory map layouts
* [netlistsvg](https://github.com/nturley/netlistsvg)
  * draws an SVG schematic from a JSON netlist
* [pcbdraw](https://github.com/yaqwsx/PcbDraw)
  * Convert KiCAD board into 2D drawing suitable for pinout diagrams
* [pinion](https://github.com/yaqwsx/Pinion)
  * Generate interactive Diagrams for your PCBs
* [pinout](https://github.com/j0ono0/pinout)
  * Python package that generates hardware pinout diagrams as SVG images
* [sphinx](https://github.com/sphinx-doc/sphinx)
  * Document builder
* [sphinx-verilog-domain](https://github.com/SymbiFlow/sphinx-verilog-domain)
  * Sphinx domain to allow integration of Verilog / SystemVerilog documentation into Sphinx.
* [sphinxcontrib-hdl-diagrams](https://github.com/SymbiFlow/sphinxcontrib-hdl-diagrams)
  * Sphinx plugin to automatically generate diagrams from RTL.
* [symbolator](https://github.com/kevinpt/symbolator)
  * HDL symbol generator
* [undulate](https://github.com/LudwigCRON/undulate)
  * Python compatible wavedrom module with extensions and console rendering support
* [wavedrom](https://github.com/wavedrom/wavedrom)
  * Digital timing diagram rendering engine
* [wavedrompy](https://github.com/wallento/wavedrompy)
  * Python comptabled Wavedrom module

## FPGA Design
* [1st-class](https://github.com/os-fpga/1st-CLaaS)
  * Framework for FPGA cloud accelerators
* [byteman](https://github.com/FPGA-Research-Manchester/byteman)
  * Bitstream relocation and manipulation tool
* [icestudio](https://github.com/FPGAwars/icestudio)
  * Visual editor for open FPGA boards
* [foedag](https://github.com/os-fpga/FOEDAG)
  * Framework Open EDA Gui
* [openfpgaloader](https://github.com/trabucayre/openFPGALoader)
  * Universal utility for programming FPGA
* [rphax](https://github.com/shariethernet/RPHAX)
  * Automation flow to develop and prototype hardware accelerators on Xilinx FPGAs
* [virtual-fpga-lab](https://github.com/os-fpga/Virtual-FPGA-Lab)
  * FPGA development in your browser

## Register Design
* [gen_registers](https://github.com/lsteveol/gen_registers)
  * Python based tool for generating hardware registers and their associated files
* [rggen](https://github.com/rggen/rggen)
  * Configuration and status register generator
* [systemrdl](https://github.com/SystemRDL/systemrdl-compiler)
  * Generic compiler front-end for Accellera's SystemRDL 2.0 register description language

# Verification

## Analog Verification
* [adc-eval](https://github.com/esynr3z/adc-eval)
  * Python tools for ADC performance analysis
* [anasysmod](https://github.com/sgherbst/anasymod)
  * Framework for FPGA emulation of mixed-signal systems
* [cvc](https://github.com/d-m-bailey/cvc)
  * CVC: Circuit Validity Checker.
* [devsim](https://github.com/devsim)
  * TCAD Semiconductor Device Simulator
* [eesim](https://github.com/danchitnis/EEsim)
  * Browser-based SPICE circuit simulator
* [lctime](https://codeberg.org/librecell/lctime)
  * Library cell characterization
* [hotspot](https://github.com/uvahotspot/HotSpot)
  * Thermal modeling tool for use in architectural studies
* [ngspice](http://ngspice.sourceforge.net/)
  * Spice simulator
* [msdsl](https://github.com/sgherbst/msdsl)
  * Automatic generation of real number models from analog circuits
* [OpenPLC_v3](https://github.com/thiagoralves/OpenPLC_v3)
  * OpenPLC Runtime version 3
* [OpenVAF](https://github.com/pascalkuthe/OpenVAF)
  * Next generation Verilog-A compiler
* [pact](https://github.com/peaclab/PACT)
  * Thermal Simulator
* [pyaedt](https://github.com/pyansys/pyaedt)
  * Ansys AEDT Python Client Package
* [pydpf-core](https://github.com/pyansys/pydpf-core)
  * Ansys core processing framework
* [pyfluent](https://github.com/pyansys/pyfluent)
  * Ansys interface to Ansys Fluent
* [pymapdl](https://github.com/pyansys/pymapdl)
  * Ansys interface to MAPDL
* [pyspice](https://github.com/PySpice-org/PySpice)
  * Python interface for ngspice and xyce
* [SimulIDE](https://github.com/SimulIDE/SimulIDE)
  * SimulIDE is a simple real-time electronic circuit simulator
* [svreal](https://github.com/sgherbst/svreal)
  * Synthesizable real number library in SystemVerilog (fixed & floating point formats)
* [xyce](https://github.com/Xyce/Xyce)
  * Parallel spice simulator from Sandia national labs

## Benchmarks
* [bsg_pipeclean_suite](https://github.com/bespoke-silicon-group/bsg_pipeclean_suite)
  * Collection of designs used to stress test new CAD flows
* [corescore](https://github.com/olofk/corescore)
  * Benchmark for FPGAs and their synthesis/P&R tools
* [epfl-benchmarks](https://github.com/lsils/benchmarks)
  * Combinational Benchmark Suite for logic synthesis
* [opdb](https://github.com/PrincetonUniversity/OPDB)
  * Princeton design benchmark generators
* [rdf-2020](https://github.com/ieee-ceda-datc/RDF-2020)
  * IEEE CEDA eda benchmark flow
* [sv-tests](https://github.com/chipsalliance/sv-tests)
  * SystemVerilog compliance test suite

## Digital Verification
* [awsteria_infra](https://github.com/bluespec/AWSteria_Infra)
  * Middleware for AWS hosted FPGA applications
* [boolector](https://github.com/boolector/boolector)
  * SMT solver for the theories of fixed-size bit-vectors, arrays and uninterpreted functions.
* [champsim](https://github.com/ChampSim/ChampSim)
  * Trace-based simulator for a microarchitecture study.
* [cocotb](https://github.com/cocotb/cocotb)
  * Coroutine based cosimulation library for writing VHDL and Verilog testbenches in Python
* [cvc5](https://github.com/cvc5/cvc5)
  * SMT automatic theorem prover
* [dromajo](https://github.com/chipsalliance/dromajo)
  * RISC-V RV64GC functional emulator
* [essent](https://github.com/ucsc-vama/essent)
  * High-performance FIRRTL (Chisel) simulator
* [firesim](https://github.com/firesim/firesim)
  * FPGA-accelerated Cycle-accurate Hardware Simulation in the Cloud
* [frame](https://github.com/maestro-project/frame)
  * Fast Roofline Analytical Modeling and Estimation
* [fstdumper](https://github.com/semify-eda/fstdumper)
  * Verilog VPI module to dump FST (Fast Signal Trace) databases
* [gem5](https://github.com/gem5/gem5)
  * Modular simulator platform for computer-system architecture research
* [ghdl](https://github.com/ghdl/ghdl)
  * VHDL 2008/93/87 simulator
* [icarus](https://github.com/steveicarus/iverilog.git)
  * Verilog IEEE-1364 simulator
* [ilang](https://github.com/PrincetonUniversity/ILAng)
  * Princeton modeling and Verification Platform for SoCs using ILAs
* [kaktus2dev](https://github.com/kactus2/kactus2dev)
  * Graphical EDA tool based on the IP-XACT standard
* [libsystemctlm-soc](https://github.com/Xilinx/libsystemctlm-soc)
  * SystemC/TLM-2.0 Co-simulation framework
* [maestro](https://github.com/maestro-project/maestro)
  * Analytical cost model evaluating DNN mappings (dataflows and tiling)
* [opensta](https://github.com/The-OpenROAD-Project/OpenSTA)
  * Signoff quality STA engine used by OpenRoad
* [opentimer](https://github.com/OpenTimer/OpenTimer)
  * High perormance static timing analysis
* [osvvm](https://github.com/OSVVM/OsvvmLibraries)
  * A VHDL verification framework
* [qemu](https://github.com/qemu/qemu)
  * Generic and open source machine & userspace emulator and virtualizer
* [pono](https://github.com/upscale-project/pono)
  * Extensible SMT-based model checker implemented in C++.
* [pyucis](https://github.com/fvutils/pyucis)
  * Python API to Unified Coverage Interoperability Standard (UCIS) Data
* [pyuvm](https://github.com/pyuvm/pyuvm)
  * SystemVerilog UVM written in Python
* [pyvsc](https://github.com/fvutils/pyvsc)
  * Python packages or SystemVerilog UVM style Verification Stimulus and Coverage
* [renode](https://github.com/renode/renode)
  * Generic and open source machine emulator
* [sby](https://github.com/YosysHQ/sby)
  * Front-end for Yosys-based formal verification flows.
* [systemctlm-cosim-demo](https://github.com/Xilinx/systemctlm-cosim-demo)
  * Demo system for libsystemctlm-soc library
* [sv_waveterm](https://github.com/PeterMonsson/sv_waveterm)
  * Generate text waves in simulation log file
* [svlint](https://github.com/dalance/svlint)
  * SystemVerilog linter
* [svlint-action](https://github.com/dalance/svlint-action)
  * GitHub action for svlint
* [tce](https://github.com/cpc/tce)
  * Application-specific instruction-set processor (ASIP) toolset
* [uvvm](https://github.com/UVVM/UVVM)
  * Library for making very structured VHDL-based testbenches.
* [verilator](https://github.com/verilator/verilator)
  * SystemVerilog simulator and lint system.
* [v2k-top](https://github.com/kev-cam/v2k-top)
  * Parser/simulation framework for Verilog & C++
* [vidbo](https://github.com/olofk/vidbo)
  * Virtual development board
* [vunit](https://github.com/VUnit/vunit)
  * Unit testing framework for VHDL/SystemVerilog
* [z3](https://github.com/Z3Prover/z3)
  * Microsoft research theorem prover.

## Waveform viewers
* [d3wave](https://github.com/Nic30/d3-wave)
  * D3.js based wave (signal) visualizer
* [gtkwave](https://github.com/gtkwave/gtkwave)
  * GTK+ based VCD waveform viewer
* [konata](https://github.com/shioyadan/Konata)
  * Instruction pipeline visualizer for Gem5
* [sigrok](https://github.com/sigrokproject)
  * Portable, signal analysis software suite (logic analyzers, scopes, multimeters, and more)
* [simview](https://github.com/pieter3d/simview)
  * Text-based SystemVerilog design browser and waveform viewer
* [sootty](https://github.com/Ben1152000/sootty)
  * Command-line tool for displaying vcd waveforms

# Designs & Generators

## Accelerators
* [aes](https://github.com/secworks/aes)
  * Symmetric block cipher AES (Advanced Encryption Standard)
* [ara](https://github.com/pulp-platform/ara)
  * Vector Unit, compatible with the RISC-V Vector Extension
* [bfg](https://github.com/growly/bfg)
  * Compiler for Reduced-Complexity Reconfigurable Fabrics
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
* [NNgen](https://github.com/NNgen/nngen)
  * A Fully-Customizable Hardware Synthesis Compiler for Deep Neural Network
* [nvdla](https://github.com/nvdla/hw)
  * NVIDIA Deep Learning Accelerator (NVDLA)
* [NyuziProcessor](https://github.com/jbush001/NyuziProcessor)
  * GPGPU microprocessor architecture
* [opencgra](https://github.com/pnnl/OpenCGRA)
  * Parametrizable Coarse-Grained Reconfigurable Array (CGRA) Generator
* [openofdm](https://github.com/jhshi/openofdm)
  * 802.11 OFDM PHY decoder
* [openspike](https://github.com/sfmth/OpenSpike)
  * Spiking neural network accelerator
* [sha3](https://github.com/ucb-bar/sha3)
  * Berkeley SHAR3 ROCC Accelerator
* [Serpens](https://github.com/linghaosong/Serpens)
  * HBM FPGA based SpMV Accelerator
* [Sextans](https://github.com/linghaosong/Sextans)
  * FPGA accelerator for general-purpose Sparse-Matrix Dense-Matrix Multiplication (SpMM)
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

## Analog Circuits
* [AMS_KGD](https://github.com/USCPOSH/AMS_KGD)
  * Repository for Known Good Analog Designs (KGDs)
* [analog_blocks](https://github.com/mabrains/Analog_blocks)
  * Basic building blocks (OTA, BandGap and LDO) in Skywater 130nm.
* [openfasoc](https://github.com/idea-fasoc/OpenFASOC)
  * Fully-Autonomous SoC Synthesis using Customizable Cell-Based Synthesizable Analog Circuits
* [open-pmic](https://github.com/westonb/open-pmic)
  * Current mode buck converter on the SKY130 PDK

## Chip Packages
* [bsg_packaging](https://github.com/bespoke-silicon-group/bsg_packaging)
  * Open-Source Hardware Accelerator Packages and Sockets

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
* [nocrouter](https://github.com/agalimberti/NoCRouter)
  * Network-on-Chip Router
* [OpenSERDES](https://github.com/SparcLab/OpenSERDES)
  * Digitally synthesizable architecture for SerDes using Skywater130
* [pymtl3-net](https://github.com/cornell-brg/pymtl3-net)
  * Cornell parameterizable OCN (on-chip network) generator
* [ravenoc](https://github.com/aignacio/ravenoc)
  * Configurable HDL NoC (Network-On-Chip)
* [tnoc](https://github.com/taichi-ishitani/tnoc)
  * Network on Chip Implementation written in SytemVerilog
* [USB3 Camera](https://github.com/circuitvalley/USB_C_Industrial_Camera_FPGA_USB3)
  * USB C Industrial Camera Project
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

## CPUs
* [a2i](https://github.com/openpower-cores/a2i)
  * A2I POWER processor core RTL (VHDL)
* [black-parrot](https://github.com/black-parrot/black-parrot)
  * Linux-capable RISC-V multicore
* [cfu-playground](https://github.com/google/CFU-Playground/)
  * Famework for playing with custom opcodes to accelerate TensorFlow Lite for Microcontrollers
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
* [muntjac](https://github.com/lowRISC/muntjac)
  * Simple 64-bit RISC-V multicore processor
* [neorv32](https://github.com/stnolting/neorv32)
  * Customizable and highly extensible MCU-class 32-bit RISC-V (VHDL)
* [OpenXiangShan](https://github.com/OpenXiangShan/XiangShan)
  * Open-source high-performance RISC-V processor
* [picorv32](https://github.com/YosysHQ/picorv32)
  * Size-Optimized RISC-V CPU
* [rocket-chip](https://github.com/chipsalliance/rocket-chip)
  * Linux capable RISC-V Rocket Chip Generator
* [rioschip](https://github.com/b224hisl/rioschip)
  * Out of order RISC-V core
* [serv](https://github.com/olofk/serv)
  * SErial RISC-V CPU
* [snitch](https://github.com/pulp-platform/snitch)
  * Lean but mean RISC-V system
* [vroom](https://github.com/MoonbaseOtago/vroom)
  * High performance RISC-V CPU
* [warp-v](https://github.com/stevehoover/warp-v)
  * TL-Verilog CPU core/many-core generator (RISC-V, etc.) with visualization

## FPGA Architectures
* [FABulous](https://github.com/FPGA-Research-Manchester/FABulous)
  * Fabric generator and CAD tools
* [fabric_team](https://github.com/ucb-cs250/fabric_team)
  * Simple Berkeley FPGA generator class project
* [OpenFPGA](https://github.com/lnis-uofu/OpenFPGA)
  * FPGA IP Generator
* [prga](https://github.com/PrincetonUniversity/prga)
  * Open-source FPGA research and prototyping framework

## Libraries
* [basejump_stl](https://github.com/bespoke-silicon-group/basejump_stl)
  * Library of SystemVerilog components
* [basic_verilog](https://github.com/pConst/basic_verilog)
  * Library of SystemVerilog components
* [common_cells](https://github.com/pulp-platform/common_cells)
  * Library of SystemVerilog components
* [hdl](https://github.com/analogdevicesinc/hdl)
  * Library of Analog Deveices specific components
* [oh](https://github.com/aolofsson/oh)
  * Library of Verilog components
* [pzbcm](https://github.com/pezy-computing/pzbcm)
  * Basic common modules
* [vlsiffra](https://github.com/antonblanchard/vlsiffra)
  * Fast and efficient standard cell based adders, multipliers and multiply-adders

## Memory
* [core_axi_cache](https://github.com/ultraembedded/core_axi_cache)
  * 128KB AXI cache (32-bit in, 256-bit out)
* [bsg_fakeram](https://github.com/bespoke-silicon-group/bsg_fakeram)
  * Fake RAM generator
* [HuanCun](https://github.com/OpenXiangShan/HuanCun)
  * Open-source high-performance non-blocking cache
* [openram](https://github.com/VLSIDA/OpenRAM)
  * Static random access memory (SRAM) compiler.
* [lake](https://github.com/StanfordAHA/lake)
  * Synthesizable memory generator

## Systems
* [caliptra](https://github.com/chipsalliance/caliptra-rtl)
  * Caliptra Root of Trust
* [Beagle_SDR_GPS](https://github.com/jks-prv/Beagle_SDR_GPS)
  * KiwiSDR: BeagleBone web-accessible GPS/SDR
* [bsg_manycore](https://github.com/bespoke-silicon-group/bsg_manycore)
  * Tile based architecture designed for computing efficiency, scalability
* [cep](https://github.com/CommonEvaluationPlatform/CEP)
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
* [SensSeq](https://github.com/EMIL-YORKU/SensSeq)
  * Mixed-signal system on chip for nanopore-based DNA sequencing
* [VerilogBoy](https://github.com/zephray/VerilogBoy)
  * Game Boy compatible machine with Verilog

----

# Other Awesome Lists

* [ben-marshall](https://github.com/ben-marshall/awesome-open-hardware-verification)
  * Hardware verification
* [clin99](https://github.com/clin99/awesome-eda)
  * EDA projects
* [computer-engineering-resources](https://github.com/rajesh-s/computer-engineering-resources)
  * A curated list of Computer Engineering/Architecture resources
* [delftopenhardware](https://github.com/delftopenhardware/awesome-open-hardware)
  * Open hardware materials
* [drom](https://github.com/drom/awesome-hdl)
  * HDL languages
* [hdl](https://github.com/hdl/awesome)
  * Hardware description resources
* [mattvenn](https://github.com/mattvenn/awesome-opensource-asic-resources)
  * ASIC resources
* [pkuzjx](https://github.com/pkuzjx/eda-collection)
  * Open source EDA resources
* [semiconduoctor-startups](https://github.com/aolofsson/awesome-semiconductor-startups)
  * Semiconductor startups
