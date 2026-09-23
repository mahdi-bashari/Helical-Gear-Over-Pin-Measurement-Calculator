# Helical Gear Over Pin Measurement Calculator

A Python-based engineering calculator for dimensional inspection of **helical gears** using the **Measurement Over Pins (MOP)** method.

This tool was developed to calculate the theoretical measurement values required for inspecting a helical gear by placing a measuring pin/roller between the gear teeth.

The application provides a graphical user interface built with **PyQt6** and performs the gear geometry calculations using Python.

---

## 🎯 Purpose

The main purpose of this project is to support the **dimensional inspection of helical gears and rack & pinion components**.

In gear manufacturing and quality control, direct measurement of the tooth profile can be difficult. The **Measurement Over Pins (MOP)** method provides a practical way to inspect the tooth geometry by measuring the distance over two or more pins positioned between the gear teeth.

The calculator determines:

* The theoretical ideal measuring pin diameter
* Measurement Over Pins using a selected/manual pin
* Measurement Over Pins using the calculated ideal pin

This can be useful for applications such as:

* Helical gears
* Pinions
* Rack & pinion systems
* Steering gear components
* Gear manufacturing inspection
* Dimensional quality control

---

## ⚙️ Input Parameters

The application accepts the following gear parameters:

| Parameter            | Symbol | Description                             |
| -------------------- | -----: | --------------------------------------- |
| Module               |    `m` | Gear module                             |
| Number of Teeth      |    `z` | Number of gear teeth                    |
| Pressure Angle       |    `α` | Reference pressure angle                |
| Helix Angle          |    `β` | Helix angle                             |
| Profile Shift Factor |    `x` | Profile shift coefficient               |
| Manual Pin Diameter  |   `dp` | Diameter of the available measuring pin |

The helix angle can be entered in:

```text
Degree
Minute
Second
```

For example:

```text
β = 22° 12' 13"
```

---

## 📐 Calculation Method

The calculation is based on involute gear geometry and the equivalent spur gear concept for helical gears.

### 1. Helix Angle Conversion

The entered helix angle is converted from degree-minute-second format into decimal degrees:

```python
beta = degree + minute / 60 + second / 3600
```

The result is then converted to radians for trigonometric calculations.

---

### 2. Equivalent Number of Teeth

For the helical gear calculation, an equivalent spur gear is used:

$$
z_v = \frac{z}{\cos^3 \beta}
$$

where:

* `z` = actual number of teeth
* `β` = helix angle
* `zᵥ` = equivalent number of teeth

The equivalent spur gear concept is also used in standard helical gear calculations. KHK provides the equivalent spur gear relationship as part of its helical gear technical reference.

---

### 3. Involute Function

The involute function is defined as:

$$
inv(\alpha)=\tan(\alpha)-\alpha
$$

This function is fundamental to involute gear geometry.

The calculator uses this relationship to determine the angular position associated with the measuring geometry.

---

### 4. Profile Shift

The calculator includes the profile shift coefficient:

$$
x
$$

Profile shift affects the tooth geometry and consequently changes the measurement over pins.

KHK's gear calculation reference also treats the profile shift coefficient as one of the fundamental parameters for calculating modified gear geometry.

---

## 📏 Ideal Pin Diameter

The program calculates a theoretical measuring pin diameter based on the gear geometry.

The calculated value is reported as:

```text
Ideal Pin Diameter
```

This represents the theoretically selected pin diameter for the measurement condition used by the implemented calculation.

---

## 📏 Measurement Over Pins (MOP)

The main inspection output is:

```text
Measure Over Pins
```

For a given pin diameter `dp`, the program calculates the expected measurement across the pins.

Two values are calculated:

### Manual Pin

```text
MOP Manual Pin
```

This is the expected measurement when using a real measuring pin whose diameter is entered by the user.

For example:

```text
Manual Pin Diameter = 4 mm
```

The program calculates the corresponding MOP value.

### Ideal Pin

```text
MOP Ideal Pin
```

This uses the calculated theoretical ideal pin diameter instead of the manually selected pin.

---

## 🔢 Numerical Solution

Part of the MOP calculation requires solving an involute-related nonlinear equation.

The program uses the **Newton-Raphson numerical method**:

$$
\phi_{n+1}
=
\phi_n-
\frac{f(\phi_n)}
{f'(\phi_n)}
$$

with:

$$
f(\phi)=\tan(\phi)-\phi-inv(\phi)
$$

This iterative method is used to determine the required angular parameter `φ`.

The iteration continues until the change between two successive solutions is smaller than:

```python
tolerance = 1e-12
```

with a maximum of:

```python
max_iteration = 100
```

---

## 🖥️ Graphical User Interface

The application uses **PyQt6**.

The GUI consists of three main sections:

```text
┌─────────────────────────────────────────┐
│          Input Parameters               │
│                                         │
│ Module                  [ 1.8 ]         │
│ Number of Teeth         [ 8   ]         │
│ Pressure Angle          [ 20  ]         │
│ Helix Angle Degree      [ 22  ]         │
│ Helix Angle Minute      [ 12  ]         │
│ Helix Angle Second      [ 13  ]         │
│ Profile Shift Factor    [ 0.5 ]         │
│ Manual Pin Diameter     [ 4   ]         │
└─────────────────────────────────────────┘

              [ CALCULATE ]

┌─────────────────────────────────────────┐
│          Calculation Results            │
│                                         │
│ Ideal Pin Diameter       xx.xxxx mm     │
│ MOP Manual Pin           xx.xxxx mm     │
│ MOP Ideal Pin            xx.xxxx mm     │
└─────────────────────────────────────────┘
```

---

## 📁 Project Structure

```text
helical-gear-over-pin-calculator/
│
├── main.py
├── ui_main.py
├── calculator.py
│
└── README.md
```

### `main.py`

Application entry point.

Responsible for creating the Qt application and launching the main window.

### `ui_main.py`

Contains the graphical user interface.

Responsibilities:

* Input fields
* Calculate button
* Result display
* Error handling
* Application styling

### `calculator.py`

Contains the engineering calculation engine.

Responsibilities:

* Angle conversion
* Equivalent gear calculation
* Involute calculations
* Profile shift calculations
* Ideal pin diameter
* Measurement Over Pins
* Newton-Raphson numerical solution

---

## 🚗 Possible Steering Application

Although the calculation engine is written as a general helical gear calculator, the same methodology can be applied to **steering rack & pinion systems**.

For example, a steering rack can be characterized using parameters such as:

```text
Module
Number of Teeth / Equivalent Geometry
Pressure Angle
Helix Angle
Profile Shift
```

and the resulting theoretical measurement can be compared against an actual laboratory measurement.

A possible inspection workflow is:

```text
CAD / Drawing
     │
     ▼
Gear Parameters
     │
     ▼
MOP Calculation
     │
     ▼
Select Measuring Pin
     │
     ▼
Measure Actual MOP
     │
     ▼
Compare With Theoretical Value
     │
     ▼
Dimensional Inspection
```

---

## 📚 Technical Reference

The calculation is based on standard involute gear geometry and helical gear relationships.

Reference:

**KHK Gears – Gear Technical Reference**

The KHK reference covers:

* Spur gear calculations
* Profile shifted gears
* Helical gears
* Normal and transverse systems
* Helical racks
* Equivalent gear relationships
* Gear geometry calculations

Reference:

[KHK Gears – Gear Technical Reference](https://khkgears.net/gear-knowledge/gear-technical-reference/calculation-gear-dimensions)

---

## 🛠️ Technologies

```text
Python
PyQt6
Math / Numerical Methods
Involute Gear Geometry
Newton-Raphson Method
```

---

## ⚠️ Engineering Note

This calculator should be treated as an engineering calculation/inspection support tool.

Before using the calculated values for production acceptance, the implemented equations should be verified against the applicable gear standard, drawing requirements, gear system definition (normal/transverse), measuring method, and the actual inspection equipment.

In particular, the definition of module and pressure angle must be consistent with the gear's normal or transverse system.

---

## 🚀 Future Improvements

Possible future developments:

* Add gear standard selection
* Support DIN / ISO gear inspection parameters
* Normal and transverse system selection
* Automatic selection of standard measuring pin diameter
* Tolerance calculation
* Actual vs. theoretical MOP comparison
* Measurement data logging
* CSV/Excel export
* PDF inspection report
* CAD parameter import
* Rack & pinion specific calculation mode
* Graphical visualization of the measuring pin and gear tooth geometry

---

## Author

Developed as an engineering calculation tool for gear dimensional inspection and rack & pinion applications.
