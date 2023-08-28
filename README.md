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

## PDKs
   * [Manufacturable PDKs](#manufacturable-pdks)
   * [Virtual PDKs](#virtual-pdks)

## Compilers
  * [Build systems](#build-systems)
  * [Circuit compilers](#circuit-compilers)
  * [FPGA compilers](#fpga-compilers)
  * [Layout compilers](#layout-compilers)

## Design and Verification Tools
  * [Benchmarks](#benchmarks)
  * [Board design](#board-design)
  * [Digital design](#digital-design)
  * [Documentation](#documentation)
  * [FPGA design](#fpga-design)
  * [Formal verification](#formal-verification)
  * [Linters](#linters)
  * [Register design](#register-design)
  * [Schematics](#scehamtics)
  * [Simulators](#simulators)
  * [Verification frameworks](#verification-frameworks)
  * [Waveform Viewers](#waveform-viewers)

## Designs & Generators
  * [Accelerators](#accelerators)
  * [Analog circuits](#analog-circuits)
  * [Chip packaging](#chip-packages)
  * [Boards](#board-designs)
  * [Connectivity](#connectivity)
  * [CPUs](#cpus)
  * [FPGA architectures](#fpga-architectures)
  * [Libraries](#libraries)
  * [Memory](#memory)
  * [Systems](#systems)

## Education
  * [Analog design](#analog-design)
  * [ASIC design](#asic-design)
  * [Digital design](#digital-design)
  * [FPGA Education](#fpga-design)

# PDKs

## Manufacturable PDKs

* [gf180](https://github.com/google/gf180mcu-pdk)
  * GlobalFoundries 180nm CMOS PDK
* [sg13g2](https://github.com/IHP-GmbH/IHP-Open-PDK)
  * IHP 130nm BiCMOS PDK
* [sky130](https://github.com/google/skywater-pdk)
  * Skywater 130nm CMOS PDK

## Virtual PDKs
* [asap7](https://github.com/The-OpenROAD-Project/asap7)
  * Predictive 7nm PDK
* [freepdk45](https://github.com/siliconcompiler/siliconcompiler/tree/main/third_party/pdks/virtual/freepdk45)
  * Predictive 45nm PDK
* [probe3.0](https://github.com/ABKGroup/PROBE3.0)
  * Process/design DTCO path finding technology


# Compilers

## Build Systems
* [bazelhdl](https://github.com/hdl/bazel_rules_hdl)
  * Bazel based hdl build system
* [bender](https://github.com/pulp-platform/bender)
  * Dependency management tool for hardware projects.
* [chipyard](https://github.com/ucb-bar/chipyard)
  * Agile RISC-V SoC Design Framework.
* [cocoon](https://github.com/pku-dasys/cocoon)
  * Infrastructure for integrated EDA
* [edalize](https://github.com/olofk/edalize)
  * Abstraction library for interfacing EDA tools.
* [f4fpga](https://github.com/chipsalliance/f4pga)
  * FPGA build system
* [flgen](https://github.com/pezy-computing/flgen)
  * Generate a filelist for EDA tools
* [fusesoc](https://github.com/olofk/fusesoc)
  * Package manager and build abstraction tool for FPGA/ASIC development.
* [hammer](https://github.com/ucb-bar/hammer)
  * Agile physical design component part of UC Berkeley Chipyard framework.
* [hwtbuildsystem](https://github.com/Nic30/hwtBuildsystem)
  * Library of utils for interaction with the vendor tools.
* [legohdl](https://github.com/c-rus/legoHDL)
  * Command line HDL package manager and development tool.
* [mflowgen](https://github.com/mflowgen/mflowgen)
  * Build-system generator for ASIC and FPGA design-space exploration.
* [siliconcompiler](https://github.com/siliconcompiler/siliconcompiler)

## Circuit Compilers
* [abc](https://github.com/berkeley-abc/abc)
  * System for sequential logic synthesis and formal verification
* [act](https://github.com/asyncvlsi/act)
  * Asynchronous circuit compiler tools
* [amaranth](https://github.com/amaranth-lang/amaranth)
  * Python based hardware design framework
* [bigspicy](https://github.com/google/bigspicy)
  * Tool for merging circuit descriptions
* [bsc](https://github.com/B-Lang-org/bsc)
  * Compiler, simulator, and tools for the Bluespec Hardware Description Language
* [calyx](https://github.com/cucapra/calyx)
  * Intermediate language and compilers that generate custom hardware accelerators
* [chisel](https://github.com/chipsalliance/chisel3)
  * Scala based hardware description language
* [circt](https://github.com/llvm/circt)
  * Circuit IR Compilers and Tools
* [circuitgraph](https://github.com/circuitgraph/circuitgraph)
  * Tools for working with circuits as graphs in python
* [circuitops](https://github.com/NVlabs/CircuitOps)
  * Infrastructure for dataset generation and model deployment in Generative AI
* [clash](https://github.com/clash-lang/clash-compiler)
  * Haskell to VHDL/Verilog/SystemVerilog compiler
* [coreir](https://github.com/rdaly525/coreir)
  * LLVM-style hardware compiler with first class support for generators
* [dfiant](https://github.com/DFiantHDL/DFiant)
  * Dataflow Hardware Description Language
* [fault](https://github.com/AUCOHL/Fault)
  * Design-for-testing (DFT) Solution
* [finn](https://github.com/Xilinx/finn)
  * Dataflow compiler for QNN inference
* [firrtl](https://github.com/chipsalliance/firrtl)
  * Intermediate Representation for RTL
* [gamma](https://github.com/maestro-project/gamma)
  * Optimizes mapping of DNN models on DNN Accelerators
* [gamora](https://github.com/Yu-Utah/Gamora)
  * Graph Learning based Symbolic Reasoning for Large-Scale Boolean Networks
* [halide](https://github.com/halide/Halide)
  * Language for fast, portable data-parallel computation
* [halide-to-hardware](https://github.com/StanfordAHA/Halide-to-Hardware)
  * Hardware generator combining halide and coreir
* [hdl21](https://github.com/dan-fritchman/Hdl21)
  * Hardware Description Library
* [hdlconvertor](https://github.com/Nic30/hdlConvertor)
  * Verilog/VHDL parser preprocessor and code generator for C++/Python based on ANTL4
* [hs-to-coq](https://github.com/plclub/hs-to-coq)
  * Convert Haskell source code to Coq source code
* [ipyxact](https://github.com/olofk/ipyxact)
  * Python-based IP-XACT parser
* [livehd](https://github.com/masc-ucsc/livehd)
  * Infrastructure for live interactive synthesis and simulation
* [llhd](https://github.com/fabianschuiki/llhd)
  * Intermediate representation for digital circuit descriptions
* [lsoracle](https://github.com/lnis-uofu/LSOracle)
  * Famework built on EPFL logic synthesis libraries.
* [lstools](https://github.com/lsils/lstools-showcase)
  * Showcase examples for EPFL logic synthesis libraries
* [kami](https://github.com/mit-plv/kami)
  * Platform for High-Level Parametric Hardware Specification and Verification
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
* [tapasco](https://github.com/esa-tu-darmstadt/tapasco)
  * Heterogeneous system composer
* [tce](https://github.com/cpc/tce)
  * Application-specific instruction-set processor (ASIP) toolset
* [uhdm](https://github.com/chipsalliance/UHDM)
  * Universal object model for IEEE SystemVerilog designs
* [verible](https://github.com/chipsalliance/verible)
  * SystemVerilog developer tools, including a parser, style-linter, and formatter
* [veriloggen](https://github.com/PyHDI/veriloggen)
  * Mixed-Paradigm Hardware Construction Framework
* [verik](https://github.com/frwang96/verik)
  * Kotlin based hardware description language
* [vlsir](https://github.com/Vlsir/Vlsir)
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
* [autodmp](https://github.com/NVlabs/AutoDMP)
  * Automated DREAMPlace-based Macro Placement
* [bag](https://github.com/ucb-art/BAG_framework)
  * Berkeley analog layout generator
* [coriolis](https://gitlab.lip6.fr/vlsi-eda/coriolis.git)
  * RTL2GDS toolchain for mature nodes
* [dreamplace](https://github.com/limbo018/DREAMPlace)
  * Deep learning toolkit-enabled VLSI placement
* [gdsfactory](https://github.com/gdsfactory/gdsfactory)
  * Platform for chip design and layout
* [gdstk](https://github.com/heitzmann/gdstk)
  * C++/Python library for creation and manipulation of GDSII and OASIS files.
* [gdspy](https://github.com/heitzmann/gdspy)
  * Python module for creating GDSII stream files, usually CAD layouts.
* [klayout](https://github.com/KLayout/klayout)
  * Layout viewer
* [lclayout](https://codeberg.org/librecell/lclayout)
  * Layout generator for CMOS standard-cells
* [layout21](https://github.com/dan-fritchman/Layout21)
  * Integrated Circuit Layout
* [magic](https://github.com/RTimothyEdwards/magic)
  * Magic VLSI layout tool
* [magical](https://github.com/magical-eda/MAGICAL)
  * Machine Generated Analog IC Layout
* [openroad](https://github.com/The-OpenROAD-Project/OpenROAD)
  * Complete RTL2GDS platform
* [phidl](https://github.com/amccaugh/phidl)
  * Python GDS layout and CAD geometry creation

# Design and Verification Tools

## Benchmarks
* [big-doe-openroad](https://github.com/msaligane/Big-DoE-OpenROAD)
  * Framework for launching massive RTL2GDS experiements
* [bringup-bench](https://github.com/toddmaustin/bringup-bench)
  * Collection of minimal programs useful for system bringup
* [bsg_pipeclean_suite](https://github.com/bespoke-silicon-group/bsg_pipeclean_suite)
  * Collection of designs used to stress test new CAD flows
* [corescore](https://github.com/olofk/corescore)
  * Benchmark for FPGAs and their synthesis/P&R tools
* [epfl-benchmarks](https://github.com/lsils/benchmarks)
  * Combinational Benchmark Suite for logic synthesis
* [fpga-tool-perf](https://github.com/chipsalliance/fpga-tool-perf)
  * FPGA tool performance profiling
* [opdb](https://github.com/PrincetonUniversity/OPDB)
  * Princeton design benchmark generators
* [rdf-2020](https://github.com/ieee-ceda-datc/RDF-2020)
  * IEEE CEDA eda benchmark flow
* [sv-tests](https://github.com/chipsalliance/sv-tests)
  * SystemVerilog compliance test suite

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
* [kicanvas](https://github.com/theacodes/kicanvas)
  * KiCAD web viewer
* [librepcb](https://github.com/LibrePCB/LibrePCB)
  * Board design framework
* [pcbflow](https://github.com/michaelgale/pcbflow)
  * Python based Printed Circuit Board (PCB) layout and design package based on CuFlow

## Digital Design
* [verilog-mode](https://www.veripool.org/verilog-mode/)
  * Popular free Verilog mode for Emacs
* [vscode-systemverilog](https://github.com/eirikpre/VSCode-SystemVerilog)
  * SystemVerilog support in VS Code
* [vscode-teroshdl](https://github.com/TerosTechnology/vscode-terosHDL)
  * Full IDE for RTL development in VS Code

## Documentation
* [graphviz](https://github.com/xflr6/graphviz)
  * Python library for graph cration and rendering in DOT language
* [gds3d](https://github.com/trilomix/GDS3D)
  * Reads GDSII layout and renders in 3D
* [kythe](https://github.com/chipsalliance/verible/blob/master/verilog/tools/kythe)
  * Verible based SystemVerilog source file indexer
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

## Formal Verification
* [boolector](https://github.com/boolector/boolector)
  * SMT solver for the theories of fixed-size bit-vectors, arrays and uninterpreted functions
* [cvc5](https://github.com/cvc5/cvc5)
  * SMT automatic theorem prover
* [ilang](https://github.com/PrincetonUniversity/ILAng)
  * Princeton modeling and Verification Platform for SoCs using ILAs
* [pono](https://github.com/upscale-project/pono)
  * Extensible SMT-based model checker implemented in C++.
* [sby](https://github.com/YosysHQ/sby)
  * Front-end for Yosys-based formal verification flows.
* [z3](https://github.com/Z3Prover/z3)
  * Microsoft research theorem prover

## Linters
* [svlint](https://github.com/dalance/svlint)
  * SystemVerilog linter
* [svlint-action](https://github.com/dalance/svlint-action)
  * GitHub action for svlint
* [verible](https://github.com/chipsalliance/verible)
  * SystemVerilog developer tools, including a parser, style-linter, and formatter
* [verilator](https://github.com/verilator/verilator)
  * SystemVerilog simulator and lint system

## Register Design
* [gen_registers](https://github.com/lsteveol/gen_registers)
  * Python based tool for generating hardware registers and their associated files
* [rggen](https://github.com/rggen/rggen)
  * Configuration and status register generator
* [open-register-design-tool](https://github.com/Juniper/open-register-design-tool)
  * Generate register RTL, models, and docs using SystemRDL or JSpec input
* [peakrdl](https://github.com/SystemRDL/PeakRDL)
  * SystemRDL based control & status register (CSR) toolchain
* [systemrdl](https://github.com/SystemRDL/systemrdl-compiler)
  * Generic compiler front-end for Accellera's SystemRDL 2.0 register description language

## Schematics
* [d3-hwschematics](https://github.com/Nic30/d3-hwschematic)
  * Schematic visualizer
* [kaktus2dev](https://github.com/kactus2/kactus2dev)
  * Graphical EDA tool based on the IP-XACT standard
* [openplc_editor](https://github.com/thiagoralves/OpenPLC_Editor)
  * IDE capable of creating programs for the OpenPLC Runtime
* [oregano](https://github.com/drahnr/oregano)
  * Schematic capture and circuit simulator
* [qucs_s](https://github.com/ra3xdh/qucs_s)
  * Integrated circuit simulator with Graphical User Interface
* [hdl21schematics](https://github.com/Vlsir/Hdl21Schematics)
  * Hdl21 Schematics
* [xschem](https://github.com/StefanSchippers/xschem)
  * Schematic editor for VLSI/Asic/Analog custom designs

## Simulators
* [champsim](https://github.com/ChampSim/ChampSim)
  * Trace-based simulator for a microarchitecture study
* [devsim](https://github.com/devsim)
  * TCAD Semiconductor Device Simulator
* [dromajo](https://github.com/chipsalliance/dromajo)
  * RISC-V RV64GC functional emulator
* [eesim](https://github.com/danchitnis/EEsim)
  * Browser-based SPICE circuit simulator
* [essent](https://github.com/ucsc-vama/essent)
  * High-performance FIRRTL (Chisel) simulator
* [femwell](https://github.com/HelgeGehring/femwell)
  * Finite element based simulation tool for integrated circuits, electric and photonic!
* [firesim](https://github.com/firesim/firesim)
  * FPGA-accelerated Cycle-accurate Hardware Simulation in the Cloud
* [gem5](https://github.com/gem5/gem5)
  * Modular simulator platform for computer-system architecture research
* [ghdl](https://github.com/ghdl/ghdl)
  * VHDL 2008/93/87 simulator
* [hotspot](https://github.com/uvahotspot/HotSpot)
  * Thermal modeling tool for use in architectural studies
* [icarus](https://github.com/steveicarus/iverilog.git)
  * Verilog IEEE-1364 simulator
* [irsim](https://github.com/RTimothyEdwards/irsim)
  * Switch-level simulator for digital circuits
* [libsystemctlm-soc](https://github.com/Xilinx/libsystemctlm-soc)
  * SystemC/TLM-2.0 Co-simulation framework
* [ngspice](http://ngspice.sourceforge.net/)
  * Spice simulator
* [nvc](https://github.com/nickg/nvc)
  * VHDL compiler and simulator
* [pact](https://github.com/peaclab/PACT)
  * Thermal simulator
* [qemu](https://github.com/qemu/qemu)
  * Generic and open source machine & userspace emulator and virtualizer
* [renode](https://github.com/renode/renode)
  * Generic and open source machine emulator
* [simulide](https://github.com/SimulIDE/SimulIDE)
  * SimulIDE is a simple real-time electronic circuit simulator
* [tiny-five](https://github.com/OpenMachine-ai/tinyfive)
  * Lightweight RISC-V emulator and assembler written entirely in Python with examples for AI/ML
* [xyce](https://github.com/Xyce/Xyce)
  * Parallel spice simulator from Sandia national labs
* [verilator](https://github.com/verilator/verilator)
  * SystemVerilog simulator and lint system

## Verification Frameworks
* [adc-eval](https://github.com/esynr3z/adc-eval)
  * Python tools for ADC performance analysis
* [awsteria_infra](https://github.com/bluespec/AWSteria_Infra)
  * Middleware for AWS hosted FPGA applications
* [anasysmod](https://github.com/sgherbst/anasymod)
  * Framework for FPGA emulation of mixed-signal systems
* [cocotb](https://github.com/cocotb/cocotb)
  * Coroutine based cosimulation library for writing VHDL and Verilog testbenches in Python
* [cocotbext-axi](https://github.com/alexforencich/cocotbext-axi)
  * AXI interface modules for Cocotb
* [cocotbext-pcie](https://github.com/alexforencich/cocotbext-pcie)
  * PCI express simulation framework for Cocotb
* [cvc](https://github.com/d-m-bailey/cvc)
  * CVC: Circuit Validity Checker
* [core-v-verif](https://github.com/openhwgroup/core-v-verif)
  * Functional verification project for the CORE-V family of RISC-V cores
* [easier-uvm](https://www.doulos.com/knowhow/systemverilog/uvm/easier-uvm)
  * UVM code generator and coding guidelines
* [force-riscv](https://github.com/openhwgroup/force-riscv)
  * Open HW Group RISC-V instruction set generator
* [fault](https://github.com/leonardt/fault)
  * Python package for testing hardware
* [frame](https://github.com/maestro-project/frame)
  * Fast Roofline Analytical Modeling and Estimation
* [fstdumper](https://github.com/semify-eda/fstdumper)
  * Verilog VPI module to dump FST (Fast Signal Trace) databases
* [lctime](https://codeberg.org/librecell/lctime)
  * Library cell characterization
* [maestro](https://github.com/maestro-project/maestro)
  * Analytical cost model evaluating DNN mappings (dataflows and tiling)
* [msdsl](https://github.com/sgherbst/msdsl)
  * Automatic generation of real number models from analog circuits
* [netgen](https://github.com/RTimothyEdwards/netgen)
  * LVS tool for comparing SPICE or verilog netlists
* [openplc_v3](https://github.com/thiagoralves/OpenPLC_v3)
  * OpenPLC Runtime version 3
* [opensta](https://github.com/The-OpenROAD-Project/OpenSTA)
  * Signoff quality STA engine used by OpenRoad
* [opentimer](https://github.com/OpenTimer/OpenTimer)
  * High performance static timing analysis
* [openvaf](https://github.com/pascalkuthe/OpenVAF)
  * Next generation Verilog-A compiler
* [osvvm](https://github.com/OSVVM/OsvvmLibraries)
  * A VHDL verification framework
* [pyspice](https://github.com/PySpice-org/PySpice)
  * Python interface for ngspice and xyce
* [pyucis](https://github.com/fvutils/pyucis)
  * Python API to Unified Coverage Interoperability Standard (UCIS) Data
* [pyuvm](https://github.com/pyuvm/pyuvm)
  * SystemVerilog UVM written in Python
* [pyvsc](https://github.com/fvutils/pyvsc)
  * Python packages or SystemVerilog UVM style Verification Stimulus and Coverage
* [raft](https://github.com/Xilinx/RAFT)
  * Rapid Abstraction FPGA Toolbox
* [rohd-cosim](https://github.com/intel/rohd-cosim)
  * Framework for cosimulation between the ROHD simulator and SystemVerilog simulators.
* [rohd-vf](https://github.com/intel/rohd-vf)
  * ROHD-based verification and testbench framework in Dart.
* [svreal](https://github.com/sgherbst/svreal)
  * Synthesizable real number library in SystemVerilog (fixed & floating point formats)
* [systemctlm-cosim-demo](https://github.com/Xilinx/systemctlm-cosim-demo)
  * Demo system for libsystemctlm-soc library
* [sv_waveterm](https://github.com/PeterMonsson/sv_waveterm)
  * Generate text waves in simulation log file
* [tvip-apb](https://github.com/taichi-ishitani/tvip-apb)
  * UVM based AMBA APB VIP
* [tvip-axi](https://github.com/taichi-ishitani/tvip-axi)
  * UVM based AMBA AXI VIP
* [uvvm](https://github.com/UVVM/UVVM)
  * Library for making very structured VHDL-based testbenches.
* [v2k-top](https://github.com/kev-cam/v2k-top)
  * Parser/simulation framework for Verilog & C++
* [vidbo](https://github.com/olofk/vidbo)
  * Virtual development board
* [vunit](https://github.com/VUnit/vunit)
  * Unit testing framework for VHDL/SystemVerilog

## Waveform Viewers
* [d3wave](https://github.com/Nic30/d3-wave)
  * D3.js based wave (signal) visualizer
* [gtkwave](https://github.com/gtkwave/gtkwave)
  * GTK+ based VCD waveform viewer
* [iio-oscilloscope](https://github.com/analogdevicesinc/iio-oscilloscope)
  * GTK+ based oscilloscope application for interfacing with various IIO devices
* [konata](https://github.com/shioyadan/Konata)
  * Instruction pipeline visualizer for Gem5
* [scopy](https://github.com/analogdevicesinc/scopy)
  * Software oscilloscope and signal analysis toolset
* [sigrok](https://github.com/sigrokproject)
  * Portable, signal analysis software suite (logic analyzers, scopes, multimeters, and more)
* [simview](https://github.com/pieter3d/simview)
  * Text-based SystemVerilog design browser and waveform viewer
* [sootty](https://github.com/Ben1152000/sootty)
  * Command-line tool for displaying vcd waveforms
* [verilog-vcd-parser](https://github.com/ben-marshall/verilog-vcd-parser)
  * Parser for Value Change Dump (VCD) files

# Designs & Generators

## Accelerators
* [aes](https://github.com/secworks/aes)
  * Symmetric block cipher AES (Advanced Encryption Standard)
* [ara](https://github.com/pulp-platform/ara)
  * Vector Unit, compatible with the RISC-V Vector Extension
* [bfg](https://github.com/growly/bfg)
  * Compiler for Reduced-Complexity Reconfigurable Fabrics
* [bismp](https://github.com/EECS-NTNU/bismo/)
  * Chisel-based bit-serial matrix multiplication accelerator generator
* [finn](https://github.com/Xilinx/finn)
  * Quantized NN to FPGA dataflow accelerator generator
* [fftgenerator](https://github.com/ucb-bar/FFTGenerator)
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
* [logicnets](https://github.com/Xilinx/logicnets)
  * Train and generate LUT-based neural networks
* [nngen](https://github.com/NNgen/nngen)
  * Fully-Customizable Hardware Synthesis Compiler for Deep Neural Network
* [nvdla](https://github.com/nvdla/hw)
  * NVIDIA Deep Learning Accelerator (NVDLA)
* [nyuziprocessor](https://github.com/jbush001/NyuziProcessor)
  * GPGPU microprocessor architecture
* [opencgra](https://github.com/pnnl/OpenCGRA)
  * Parametrizable Coarse-Grained Reconfigurable Array (CGRA) Generator
* [openofdm](https://github.com/jhshi/openofdm)
  * 802.11 OFDM PHY decoder
* [openspike](https://github.com/sfmth/OpenSpike)
  * Spiking neural network accelerator
* [sha3](https://github.com/ucb-bar/sha3)
  * Berkeley SHAR3 ROCC Accelerator
* [serpens](https://github.com/linghaosong/Serpens)
  * HBM FPGA based SpMV Accelerator
* [sextans](https://github.com/linghaosong/Sextans)
  * FPGA accelerator for Sparse-Matrix Dense-Matrix Multiplication (SpMM)
* [spiral](https://github.com/spiral-software/spiral-software)
  * Spiral based FFT generator
* [tvm-vta](https://github.com/apache/tvm-vta)
  * Opwn, modular, deep learning accelerator
* [verigood-ml](https://github.com/VeriGOOD-ML/public)
  * Verilog Generator, Optimized for Designs for Machine Learning
* [verigpu](https://github.com/hughperkins/VeriGPU)
  * OpenSource GPU, loosely based on RISC-V ISA
* [verilog-lfsr](https://github.com/alexforencich/verilog-lfsr)
  * Parametrizable combinatorial parallel LFSR/CRC module
* [vortex](https://github.com/vortexgpgpu/vortex)
  * Full-system RISCV-based GPGPU processor

## Analog Circuits
* [ams_kgd](https://github.com/USCPOSH/AMS_KGD)
  * Repository for Known Good Analog Designs (KGDs)
* [analog_blocks](https://github.com/mabrains/Analog_blocks)
  * Basic building blocks (OTA, BandGap and LDO) in Skywater 130nm.
* [openfasoc](https://github.com/idea-fasoc/OpenFASOC)
  * Automated Mixed Signal SoC Synthesis Framework
* [open-pmic](https://github.com/westonb/open-pmic)
  * Current mode buck converter on the SKY130 PDK

## Chip Packaging
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
* [ctucanfd_ip_core](https://gitlab.fel.cvut.cz/canbus/ctucanfd_ip_core)
  * CAN with Flexible Data-rate IP Core developed at Department of Measurement of FEE CTU
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
* [openserdes](https://github.com/SparcLab/OpenSERDES)
  * Digitally synthesizable architecture for SerDes using Skywater130
* [pymtl3-net](https://github.com/cornell-brg/pymtl3-net)
  * Cornell parameterizable OCN (on-chip network) generator
* [ravenoc](https://github.com/aignacio/ravenoc)
  * Configurable HDL NoC (Network-On-Chip)
* [tnoc](https://github.com/taichi-ishitani/tnoc)
  * Network on Chip Implementation written in SytemVerilog
* [usb3_camera](https://github.com/circuitvalley/USB_C_Industrial_Camera_FPGA_USB3)
  * USB C Industrial Camera Project
* [usb_cdc](https://github.com/ulixxe/usb_cdc/)
  * Minimal USB CDC (ACM) implementation in verilog
* [usb_dfu](https://github.com/ulixxe/usb_dfu/tree/main)
  * Verilog implementation of the USB Device Class Specification for Device Firmware Upgrade (DFU), version 1.1
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
* [vis4mesh](https://github.com/ueqri/vis4mesh)
  * Visualization tool for designing mesh Network-on-Chips
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
* [ara](https://github.com/pulp-platform/ara)
  * 64-bit Vector unit coprocessor to Ccva6
* [black-parrot](https://github.com/black-parrot/black-parrot)
  * Linux-capable RISC-V multicore
* [cfu-playground](https://github.com/google/CFU-Playground/)
  * Famework for playing with custom opcodes to accelerate TensorFlow Lite for Microcontrollers
* [cores-swerv](https://github.com/chipsalliance/Cores-SweRV)
  * SweRV EH1 RISC-Vcore
* [cores-swerv-el2](https://github.com/chipsalliance/Cores-SweRV-EL2)
  * SweRV EL2 RISC-V Core
* [core-v-verif](https://github.com/openhwgroup/core-v-verif)
  * Functional verification project for the CORE-V family of RISC-V cores
* [cva6](https://github.com/openhwgroup/cva6)
  * Linux capable RISC-V CPU
* [cve2](https://github.com/openhwgroup/cve2)
  * Small two-stage 32 bit RISC-V CPU core (RV32IMC/EMC)
* [cv32e40x](https://github.com/openhwgroup/cv32e40x)
  * RV32IMFCX RISC-V 4-stage RISC-V CPU
* [cvw](https://github.com/openhwgroup/cvw)
  * Configurable RISC-V Processor for RISC-V System-on-Chip Design textbook.
* [ibex](https://github.com/lowRISC/ibex)
  * Small 32 bit RISC-V CPU core
* [lizard](https://github.com/cornell-brg/lizard)
  * Cornell modular RV64IM Out-of-Order Processor Built with PyMTL
* [microwatt](https://github.com/antonblanchard/microwatt)
  * Open POWER ISA softcore written in VHDL 2008
* [minimax](https://github.com/gsmecher/minimax)
  * A Compressed-First, Microcoded RISC-V CPU
* [muntjac](https://github.com/lowRISC/muntjac)
  * Simple 64-bit RISC-V multicore processor
* [neorv32](https://github.com/stnolting/neorv32)
  * Customizable and highly extensible MCU-class 32-bit RISC-V (VHDL)
* [openxiangshan](https://github.com/OpenXiangShan/XiangShan)
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
* [veer](https://github.com/chipsalliance/Cores-VeeR-EL2)
  * 32-bit integer machine-mode RISC-V CPU
* [vroom](https://github.com/MoonbaseOtago/vroom)
  * High performance RISC-V CPU

## FPGA Architectures
* [fabulous](https://github.com/FPGA-Research-Manchester/FABulous)
  * Fabric generator and CAD tools
* [fabric_team](https://github.com/ucb-cs250/fabric_team)
  * Simple Berkeley FPGA generator class project
* [openfpga](https://github.com/lnis-uofu/OpenFPGA)
  * FPGA IP Generator
* [prga](https://github.com/PrincetonUniversity/prga)
  * Open-source FPGA research and prototyping framework

## Libraries
* [basejump_stl](https://github.com/bespoke-silicon-group/basejump_stl)
  * Library of SystemVerilog components
* [basic_verilog](https://github.com/pConst/basic_verilog)
  * Library of SystemVerilog components
* [berkeley-hardfloat](https://github.com/ucb-bar/berkeley-hardfloat)
  * Berkeley hardware floating point units
* [common_cells](https://github.com/pulp-platform/common_cells)
  * Library of SystemVerilog components
* [cvfpu](https://github.com/openhwgroup/cvfpu)
  * Parametric floating-point unit
* [hdl](https://github.com/analogdevicesinc/hdl)
  * Library of Analog Deveices specific components
* [oh](https://github.com/aolofsson/oh)
  * Library of Verilog components
* [pzbcm](https://github.com/pezy-computing/pzbcm)
  * Basic common modules
* [rohd-hcl](https://github.com/intel/rohd-hcl)
  * Library of reusable & configurable hardware components developed with ROHD
* [vlsiffra](https://github.com/antonblanchard/vlsiffra)
  * Fast and efficient standard cell based adders, multipliers and multiply-adders

## Memory
* [core_axi_cache](https://github.com/ultraembedded/core_axi_cache)
  * 128KB AXI cache (32-bit in, 256-bit out)
* [cv-hpdcache](https://github.com/openhwgroup/cv-hpdcache)
  * High-Performance L1 Dcache
* [bsg_fakeram](https://github.com/bespoke-silicon-group/bsg_fakeram)
  * Fake RAM generator
* [huancun](https://github.com/OpenXiangShan/HuanCun)
  * Open-source high-performance non-blocking cache
* [openram](https://github.com/VLSIDA/OpenRAM)
  * Static random access memory (SRAM) compiler.
* [lake](https://github.com/StanfordAHA/lake)
  * Synthesizable memory generator

## Systems
* [caliptra](https://github.com/chipsalliance/caliptra)
  * Caliptra Root of Trust Architecture
* [caliptra-rtl](https://github.com/chipsalliance/caliptra-rtl)
  * Caliptra Root of Trust (RTL)
* [beagle_sdr_gps](https://github.com/jks-prv/Beagle_SDR_GPS)
  * KiwiSDR: BeagleBone web-accessible GPS/SDR
* [bsg_manycore](https://github.com/bespoke-silicon-group/bsg_manycore)
  * Tile based architecture designed for computing efficiency, scalability
* [cep](https://github.com/CommonEvaluationPlatform/CEP)
  * RISC-V based Common Evaluation Platform (CEP)
* [esp](https://github.com/sld-columbia/esp)
  * Heterogeneous SoC architecture and IP design platform
* [falcon](https://github.com/falkenber9/falcon)
  * Fast Analysis of LTE Control channels
* [hero](https://github.com/pulp-platform/hero)
  * FPGA-based research platform for heterogeneous design
* [litex](https://github.com/enjoy-digital/litex)
  * SoC builder framework
* [openfasoc](https://github.com/idea-fasoc/OpenFASOC)
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
* [senseq](https://github.com/EMIL-YORKU/SensSeq)
  * Mixed-signal system on chip for nanopore-based DNA sequencing
* [verilogboy](https://github.com/zephray/VerilogBoy)
  * Game Boy compatible machine with Verilog
* [wulpus](https://github.com/pulp-bio/wulpus)
  * Wearable low-power ultrasound probe
* [x-heep](https://github.com/esl-epfl/x-heep)
  * Extendable and configurable RISC-V SoC

# Education

## Analog Design

## ASIC Design

## Board Design

## Digital Design

## FPGA Design

----

# Other Awesome Lists

* [ben-marshall](https://github.com/ben-marshall/awesome-open-hardware-verification)
  * Hardware verification
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
