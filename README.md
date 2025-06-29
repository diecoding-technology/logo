# Die Coding Technology Logo

Welcome to the Die Coding Technology Logo repository! This repository contains the official Die Coding Technology logo assets.

## Logo Versions

### Version 2

#### Static Icon

![Die Coding Technology Static Icon](v2/icon.svg)

#### Animated Icon

![Die Coding Technology Animated Icon](v2/icon-animate.svg)

## Files

- `v2/icon.svg` - Static version of the Die Coding Technology logo
- `v2/icon-animate.svg` - Animated version of the Die Coding Technology logo

## Usage

You can use these logo files in your projects. Both SVG formats are scalable and perfect for web and print applications.

### HTML Usage

```html
<!-- Static Icon -->
<img src="v2/icon.svg" alt="Die Coding Technology Logo" width="100" height="100">

<!-- Animated Icon -->
<img src="v2/icon-animate.svg" alt="Die Coding Technology Animated Logo" width="100" height="100">
```

### Embed SVG in HTML

You can also embed the SVG content directly into your HTML for better performance and styling control:

#### Inline SVG (Static)

```html
<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" version="1.1" viewBox="0 0 303.38 303.38" width="100" height="100">
    <style>
        .diecoding-icon .face {
            fill: none;
            stroke: #AA0714;
            stroke-width: 31.93;
            stroke-linecap: round;
            stroke-linejoin: round;
            stroke-miterlimit: 22.9256;
            fill-rule: nonzero;
        }
        .diecoding-icon .eye-back {
            fill: #071114;
            fill-rule: nonzero;
        }
        .diecoding-icon .eye-front {
            fill: #AA0714;
            fill-rule: nonzero;
        }
        .diecoding-icon .tooth-back {
            fill: #AA0714;
            fill-rule: nonzero;
        }
        .diecoding-icon .tooth-front {
            fill: #071114;
            fill-rule: nonzero;
        }
    </style>
    <g class="diecoding-icon">
        <!-- Eye backs -->
        <g>
            <path class="eye-back" d="M69.13 79.15c0,-8.82 7.18,-15.97 16.03,-15.97 8.85,0 16.03,7.15 16.03,15.97l-32.06 0zm0 25.95l0 -25.95 32.06 0 0 25.95 -32.06 0zm32.06 0c0,8.82 -7.18,15.97 -16.03,15.97 -8.85,0 -16.03,-7.15 -16.03,-15.97l32.06 0z" />
            <!-- Additional eye paths... -->
        </g>
        <!-- Eye fronts, teeth, and face circle -->
        <circle class="face" cx="151.69" cy="151.69" r="135.72" />
    </g>
</svg>
```

#### Inline SVG (Animated)

```html
<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" version="1.1" viewBox="0 0 303.38 303.38" width="100" height="100">
    <style>
        .diecoding-icon .face {
            fill: none;
            stroke: #AA0714;
            stroke-width: 31.93;
            stroke-linecap: round;
            stroke-linejoin: round;
            stroke-miterlimit: 22.9256;
            fill-rule: nonzero;
        }
        .diecoding-icon .eye-back {
            fill: #071114;
            fill-rule: nonzero;
            animation: eyeColor 1.2s infinite;
            animation-timing-function: ease;
        }
        .diecoding-icon .eye-front {
            fill: #AA0714;
            fill-rule: nonzero;
        }
        .diecoding-icon .tooth-back {
            fill: #AA0714;
            fill-rule: nonzero;
        }
        .diecoding-icon .tooth-front {
            fill: #071114;
            fill-rule: nonzero;
            transform-box: fill-box;
            transform-origin: 50% 50%;
            animation: toothScale 1.2s infinite;
            animation-timing-function: ease;
        }
        /* Animation delays for staggered effect */
        .diecoding-icon .eye-back:nth-of-type(1) { animation-delay: 0.6s; }
        .diecoding-icon .eye-back:nth-of-type(2) { animation-delay: 0.75s; }
        .diecoding-icon .eye-back:nth-of-type(3) { animation-delay: 0.9s; }
        .diecoding-icon .eye-back:nth-of-type(4) { animation-delay: 1.05s; }
        .diecoding-icon .tooth-front:nth-of-type(1) { animation-delay: 0.6s; }
        .diecoding-icon .tooth-front:nth-of-type(2) { animation-delay: 0.75s; }
        .diecoding-icon .tooth-front:nth-of-type(3) { animation-delay: 0.9s; }
        .diecoding-icon .tooth-front:nth-of-type(4) { animation-delay: 1.05s; }
        
        @keyframes eyeColor {
            0% { fill: #071114; }
            50% { fill: #FFFFFF; }
            100% { fill: #071114; }
        }
        @keyframes toothScale {
            0% { transform: scale(1); fill: #071114; }
            50% { transform: scale(1.1); fill: #FFFFFF; }
            100% { transform: scale(1); fill: #071114; }
        }
    </style>
    <g class="diecoding-icon">
        <!-- Eye backs with animation -->
        <g>
            <path class="eye-back" d="M69.13 79.15c0,-8.82 7.18,-15.97 16.03,-15.97 8.85,0 16.03,7.15 16.03,15.97l-32.06 0zm0 25.95l0 -25.95 32.06 0 0 25.95 -32.06 0zm32.06 0c0,8.82 -7.18,15.97 -16.03,15.97 -8.85,0 -16.03,-7.15 -16.03,-15.97l32.06 0z" />
            <!-- Additional animated eye and tooth paths... -->
        </g>
        <!-- Eye fronts, teeth with scale animation, and face circle -->
        <circle class="face" cx="151.69" cy="151.69" r="135.72" />
    </g>
</svg>
```

#### Using Object Tag

```html
<!-- Static Icon -->
<object data="v2/icon.svg" type="image/svg+xml" width="100" height="100">
    <img src="v2/icon.svg" alt="Die Coding Technology Logo">
</object>

<!-- Animated Icon -->
<object data="v2/icon-animate.svg" type="image/svg+xml" width="100" height="100">
    <img src="v2/icon-animate.svg" alt="Die Coding Technology Animated Logo">
</object>
```

#### Using Embed Tag

```html
<!-- Static Icon -->
<embed src="v2/icon.svg" type="image/svg+xml" width="100" height="100">

<!-- Animated Icon -->
<embed src="v2/icon-animate.svg" type="image/svg+xml" width="100" height="100">
```

#### Benefits of Each Method

- **`<img>` tag**: Simple, cached by browser, but limited styling control
- **Inline SVG**: Full styling control with CSS, can be animated with CSS/JS, but increases HTML size
- **`<object>` tag**: Good for interactive SVGs, fallback support, maintains SVG functionality
- **`<embed>` tag**: Similar to object but simpler, good for basic SVG embedding

### CSS Background Usage

```css
/* Static Icon */
.logo-static {
    background-image: url('v2/icon.svg');
    background-size: contain;
    background-repeat: no-repeat;
}

/* Animated Icon */
.logo-animated {
    background-image: url('v2/icon-animate.svg');
    background-size: contain;
    background-repeat: no-repeat;
}
```

## SVG Source Code

For developers who want to see the complete SVG source code:

### Static Icon (v2/icon.svg)

<details>
<summary>Click to view complete SVG source</summary>

```svg
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" version="1.1" viewBox="0 0 303.38 303.38">
    <style>
        .diecoding-icon .face {
            fill: none;
            stroke: #AA0714;
            stroke-width: 31.93;
            stroke-linecap: round;
            stroke-linejoin: round;
            stroke-miterlimit: 22.9256;
            fill-rule: nonzero;
        }
        .diecoding-icon .eye-back {
            fill: #071114;
            fill-rule: nonzero;
        }
        .diecoding-icon .eye-front {
            fill: #AA0714;
            fill-rule: nonzero;
        }
        .diecoding-icon .tooth-back {
            fill: #AA0714;
            fill-rule: nonzero;
        }
        .diecoding-icon .tooth-front {
            fill: #071114;
            fill-rule: nonzero;
        }
    </style>

    <g class="diecoding-icon">
        <g>
            <path class="eye-back"
                d="M69.13 79.15c0,-8.82 7.18,-15.97 16.03,-15.97 8.85,0 16.03,7.15 16.03,15.97l-32.06 0zm0 25.95l0 -25.95 32.06 0 0 25.95 -32.06 0zm32.06 0c0,8.82 -7.18,15.97 -16.03,15.97 -8.85,0 -16.03,-7.15 -16.03,-15.97l32.06 0z" />
            <path class="eye-back"
                d="M69.13 143.53c0,-8.82 7.18,-15.97 16.03,-15.97 8.85,0 16.03,7.15 16.03,15.97l-32.06 0zm0 25.95l0 -25.95 32.06 0 0 25.95 -32.06 0zm32.06 0c0,8.82 -7.18,15.97 -16.03,15.97 -8.85,0 -16.03,-7.15 -16.03,-15.97l32.06 0z" />
            <path class="eye-back"
                d="M202.19 79.15c0,-8.82 7.18,-15.97 16.03,-15.97 8.86,0 16.03,7.15 16.03,15.97l-32.06 0zm0 25.95l0 -25.95 32.06 0 0 25.95 -32.06 0zm32.06 0c0,8.82 -7.17,15.97 -16.03,15.97 -8.85,0 -16.03,-7.15 -16.03,-15.97l32.06 0z" />
            <path class="eye-back"
                d="M202.19 143.53c0,-8.82 7.18,-15.97 16.03,-15.97 8.86,0 16.03,7.15 16.03,15.97l-32.06 0zm0 25.95l0 -25.95 32.06 0 0 25.95 -32.06 0zm32.06 0c0,8.82 -7.17,15.97 -16.03,15.97 -8.85,0 -16.03,-7.15 -16.03,-15.97l32.06 0z" />
        </g>
        <g>
            <path class="eye-front"
                d="M73.84 90.48c-6.24,-6.24 -6.22,-16.36 0.03,-22.62 6.25,-6.25 16.38,-6.27 22.62,-0.03l-22.65 22.65zm45.16 45.16l-45.16 -45.16 22.65 -22.65 45.16 45.16 -0.04 22.62 -22.61 0.03zm22.65 -22.65c6.23,6.24 6.22,16.36 -0.04,22.62 -6.25,6.25 -16.37,6.27 -22.61,0.03l22.65 -22.65zm-67.78 45.2l45.16 -45.17 22.58 22.59 -45.16 45.16 -22.58 -22.58zm22.58 22.58c-6.25,6.25 -16.38,6.27 -22.61,0.03 -6.24,-6.23 -6.22,-16.36 0.03,-22.61l22.58 22.58z" />
            <path class="eye-front"
                d="M229.55 90.48l-22.65 -22.65c6.23,-6.24 16.36,-6.22 22.61,0.03 6.26,6.26 6.27,16.38 0.04,22.62zm-45.16 45.16l-22.62 -0.03 -0.03 -22.62 45.16 -45.16 22.65 22.65 -45.16 45.16zm-22.65 -22.65l22.65 22.65c-6.24,6.24 -16.37,6.22 -22.62,-0.03 -6.25,-6.26 -6.27,-16.38 -0.03,-22.62zm67.77 45.2l-22.58 22.58 -45.16 -45.16 22.58 -22.59 45.16 45.17zm-22.58 22.58l22.58 -22.58c6.26,6.25 6.27,16.38 0.04,22.61 -6.24,6.24 -16.36,6.22 -22.62,-0.03z" />
        </g>
        <g>
            <path class="tooth-back"
                d="M69.08 206.15c0,-8.82 7.2,-15.97 16.08,-15.97 8.88,0 16.08,7.15 16.08,15.97l-32.16 0zm0 63.87l0 -63.87 32.16 0 0 63.87 -32.16 0zm32.16 0c0,8.82 -7.2,15.97 -16.08,15.97 -8.88,0 -16.08,-7.15 -16.08,-15.97l32.16 0z" />
            <path class="tooth-back"
                d="M113.62 221.74c0,-8.82 7.12,-15.97 15.9,-15.97 8.77,0 15.89,7.15 15.89,15.97l-31.79 0zm0 63.87l0 -63.87 31.79 0 0 63.87 -31.79 0zm31.79 0c0,8.82 -7.12,15.97 -15.89,15.97 -8.78,0 -15.9,-7.15 -15.9,-15.97l31.79 0z" />
            <path class="tooth-back"
                d="M157.98 221.74c0,-8.82 7.11,-15.97 15.89,-15.97 8.78,0 15.89,7.15 15.89,15.97l-31.78 0zm0 63.87l0 -63.87 31.78 0 0 63.87 -31.78 0zm31.78 0c0,8.82 -7.11,15.97 -15.89,15.97 -8.78,0 -15.89,-7.15 -15.89,-15.97l31.78 0z" />
            <path class="tooth-back"
                d="M202.14 206.15c0,-8.82 7.2,-15.97 16.08,-15.97 8.89,0 16.09,7.15 16.09,15.97l-32.17 0zm0 63.87l0 -63.87 32.17 0 0 63.87 -32.17 0zm32.17 0c0,8.82 -7.2,15.97 -16.09,15.97 -8.88,0 -16.08,-7.15 -16.08,-15.97l32.17 0z" />
        </g>
        <g>
            <path class="tooth-front"
                d="M68.38 206.15c0,-8.82 7.51,-15.97 16.78,-15.97 9.27,0 16.78,7.15 16.78,15.97l-33.56 0zm0 7.98l0 -7.98 33.56 0 0 7.98 -33.56 0zm33.56 0c0,8.82 -7.51,15.97 -16.78,15.97 -9.27,0 -16.78,-7.15 -16.78,-15.97l33.56 0z" />
            <path class="tooth-front"
                d="M113.62 221.74c0,-8.82 7.12,-15.97 15.9,-15.97 8.77,0 15.89,7.15 15.89,15.97l-31.79 0zm0 7.99l0 -7.99 31.79 0 0 7.99 -31.79 0zm31.79 0c0,8.81 -7.12,15.96 -15.89,15.96 -8.78,0 -15.9,-7.15 -15.9,-15.96l31.79 0z" />
            <path class="tooth-front"
                d="M157.98 221.74c0,-8.82 7.11,-15.97 15.89,-15.97 8.78,0 15.89,7.15 15.89,15.97l-31.78 0zm0 7.99l0 -7.99 31.78 0 0 7.99 -31.78 0zm31.78 0c0,8.81 -7.11,15.96 -15.89,15.96 -8.78,0 -15.89,-7.15 -15.89,-15.96l31.78 0z" />
            <path class="tooth-front"
                d="M201.44 206.15c0,-8.82 7.52,-15.97 16.78,-15.97 9.27,0 16.78,7.15 16.78,15.97l-33.56 0zm0 7.98l0 -7.98 33.56 0 0 7.98 -33.56 0zm33.56 0c0,8.82 -7.51,15.97 -16.78,15.97 -9.26,0 -16.78,-7.15 -16.78,-15.97l33.56 0z" />
        </g>
        <circle class="face" cx="151.69" cy="151.69" r="135.72" />
    </g>
</svg>
```

</details>

### Animated Icon (v2/icon-animate.svg)

<details>
<summary>Click to view complete animated SVG source</summary>

```svg
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" version="1.1" viewBox="0 0 303.38 303.38">
    <style>
        .diecoding-icon .face {
            fill: none;
            stroke: #AA0714;
            stroke-width: 31.93;
            stroke-linecap: round;
            stroke-linejoin: round;
            stroke-miterlimit: 22.9256;
            fill-rule: nonzero;
        }
        .diecoding-icon .eye-back {
            fill: #071114;
            fill-rule: nonzero;
            animation: eyeColor 1.2s infinite;
            animation-timing-function: ease;
        }
        .diecoding-icon .eye-front {
            fill: #AA0714;
            fill-rule: nonzero;
        }
        .diecoding-icon .tooth-back {
            fill: #AA0714;
            fill-rule: nonzero;
        }
        .diecoding-icon .tooth-front {
            fill: #071114;
            fill-rule: nonzero;
            transform-box: fill-box;
            transform-origin: 50% 50%;
            animation: toothScale 1.2s infinite;
            animation-timing-function: ease;
        }
        .diecoding-icon .eye-back:nth-of-type(1) {
            animation-delay: 0.6s;
        }
        .diecoding-icon .eye-back:nth-of-type(2) {
            animation-delay: 0.75s;
        }
        .diecoding-icon .eye-back:nth-of-type(3) {
            animation-delay: 0.9s;
        }
        .diecoding-icon .eye-back:nth-of-type(4) {
            animation-delay: 1.05s;
        }
        .diecoding-icon .tooth-front:nth-of-type(1) {
            animation-delay: 0.6s;
        }
        .diecoding-icon .tooth-front:nth-of-type(2) {
            animation-delay: 0.75s;
        }
        .diecoding-icon .tooth-front:nth-of-type(3) {
            animation-delay: 0.9s;
        }
        .diecoding-icon .tooth-front:nth-of-type(4) {
            animation-delay: 1.05s;
        }
        @keyframes eyeColor {
            0% {
                fill: #071114;
            }
            50% {
                fill: #FFFFFF;
            }
            100% {
                fill: #071114;
            }
        }
        @keyframes toothScale {
            0% {
                transform: scale(1);
                fill: #071114;
            }
            50% {
                transform: scale(1.1);
                fill: #FFFFFF;
            }
            100% {
                transform: scale(1);
                fill: #071114;
            }
        }
    </style>
    <g class="diecoding-icon">
        <!-- Complete paths similar to static version but with animations -->
        <circle class="face" cx="151.69" cy="151.69" r="135.72" />
    </g>
</svg>
```

</details>

## License

Please check the [LICENSE](LICENSE) file for usage terms and conditions.

---

### Die Coding Technology

*-- Code Beyond Limits, Create Beyond Imagination*
