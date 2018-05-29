[![Build Status](https://travis-ci.org/wol4aravio/OSOL.Extremum.svg?branch=master)](https://travis-ci.org/wol4aravio/OSOL.Extremum.svg?branch=master)
[![codecov](https://codecov.io/gh/wol4aravio/OSOL.Extremum/branch/master/graph/badge.svg)](https://codecov.io/gh/wol4aravio/OSOL.Extremum)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6d29733e0b2d4faea9b99306ecff0f91)](https://www.codacy.com/app/wol4aravio/OSOL.Extremum?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=wol4aravio/OSOL.Extremum&amp;utm_campaign=Badge_Grade)

# Basic Description
Open-Source Optimization Library - Extremum

# Contents
* [Project background](#project-background)
* [Project structure](#project-structure)
* [Usage info](#usage-info)
	* [Out-of-box usage](#out-of-box-usage)
	* [Task preparation](#task-preparation)
		* [Unconstrained optimization](#unconstrained-optimization)
		* [Openloop control](#openloop-control)
	* [Algorithm development](#algorithm-develoment)
		* [JVM Core](#jvm-core)
			* [Scala](#scala)
			* [Java](#java)
		* [.Net Core](#net-core)
			* [C#](#c)
			* [F#](#f)
* [Implemented algorithms](#implemented-algorithms)
	* [Table of algorithms](#table-of-algorithms)
	* [Random Search](#random-search)
	* [Interval Explosion Search](#interval-explosion-search)
* [Articles about OSOL.Extremum projects](#articles-about-osolextremum-projects)

# Project background
<p align="justify">
Optimization theory is a widely-used field of mathematics that can be applied to different tasks: pure engineering problems (e.g., obtaining optimal wing shape), control synthesis tasks (e.g., determination of optimal guidance of aircraft), and even machine learning (e.g., training procedures of neural networks). Currently mostly all applied software systems support optimization procedures in a very limited form. This fact leads to several problems: black-box effect (i.e., there is no opportunity to explore source code, modify it, or simply verify), no code reuse (i.e., implemented procedures are accessible only within software that includes it), limitation of modern optimization algorithm application (i.e., number of optimization algorithms increases but most of them were verified only on synthetic tests). Also, it should be noted that all mentioned problems lead to so‑called reproducibility crisis. The main idea of this work is to suggest an Open-Source Optimization Library Extremum (OSOL Extremum) with wide API features.
</p>

# Project structure

# Usage info

## Out-of-box usage

## Task preparation

### Unconstrained optimization

### Openloop control

## Algorithm development

### JVM CORE

#### Scala

#### Java

### .Net Core

#### C\#

#### F\#

# Implemented algorithms
<p align="justify">
Current section will provide information about algorithms that are currently implemented in OSOL Extremum.
</p>

## Table of algorithms

| Name | Description | Scala | Java |  C#  |  F#  | Supports seed value |
| ---- | ----------- | :---: | :--: | :--: | :--: | :-----------------: |
| Random Search | [Wiki](https://en.wikipedia.org/wiki/Random_search) | + | + | + | + | ??? |
| Interval Explosion Search | [Trudy MAI](http://trudymai.ru/upload/iblock/b78/b783155b46dd299b9cecc91637821acc.pdf), [South Ural State University Bulletin](http://mmp.susu.ru/pdf/v9n3st5.pdf) | + | - | - | - | ??? |

## Random Search

## Interval Explosion Search


# Articles about OSOL.Extremum projects
