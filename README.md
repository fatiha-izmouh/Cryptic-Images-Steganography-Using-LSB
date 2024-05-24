# Cryptic-Images-Steganography-Using-LSB

## Overview

This project demonstrates how to hide and reveal secret messages within images using the Least Significant Bit (LSB) steganography technique. The project includes a graphical user interface (GUI) for ease of use, allowing users to select images, embed secret messages, and retrieve hidden messages.

## Features

- Hide messages within images using LSB technique.
- Reveal hidden messages from images.
- Simple and intuitive GUI built with Tkinter.
- Supports PNG and JPEG image formats.
- Dark theme for better visual appeal.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [GUI Preview](#gui-preview)
- [License](#license)

## Installation

1. Clone the repository:

    bash
    git clone https://github.com/yourusername/steganography-lsb.git
    

2. Navigate to the project directory:

    bash
    cd steganography-lsb
    

3. Install the required dependencies:

    bash
    pip install -r requirements.txt
    

## Usage

1. Run the application:

    bash
    python steganography.py
    

2. Use the GUI to select an image, enter a message, and hide/reveal messages.

## How It Works

### Concepts de Base

*Représentation Binaire*

Les données sont représentées sous forme binaire, où chaque élément est représenté par des bits (0 et 1).

### Représentation des Images

*Comment les Images sont Stockées*

Les images sont constituées de pixels, chaque pixel ayant des canaux de couleur (RGB). La couleur de chaque pixel est représentée en binaire. Par exemple, un pixel avec des valeurs RGB (255, 0, 0) est représenté en binaire comme 11111111 00000000 00000000.

### Techniques de Stéganographie

*Méthode LSB (Least Significant Bit)*

La technique LSB cache des données en modifiant le bit de poids faible de chaque canal de couleur des pixels. Par exemple, en modifiant le bit de poids faible, on peut encoder des données binaires sans modifier de manière significative l'apparence de l'image.

## GUI Preview

![GUI Preview](gui_preview.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
