# Automated Poster Composition in GIMP

This repository showcases a Python script designed to automate the composition of a visually captivating poster using GIMP. Inspired by the book *The Garden Tantra*, the script utilizes GIMP's Python API (PDB) to create a layered design featuring custom typography, shadows, highlights, and artistic motifs that blend Norwegian and Indian wildlife elements.

## Key Features

- **Automated Layer Creation**: Script generates layers for text, images, and design elements, ensuring precision and efficiency.
- **Custom Typography**: Includes support for external fonts like "Black Knife Demo" with adjustable line spacing (-150 leading) for artistic text formatting.
- **Color Palette**: Uses a limited but striking color scheme with variations of green, balanced by reds and blues.
- **Shadows and Highlights**: Implements shadow effects and highlights on text layers for enhanced readability and depth.
- **Design Principles**: Applies balance, proximity, alignment, unity, emphasis, and rhythm to achieve a harmonious composition.

## Tools and Technologies

- **Programming Language**: Python
- **Image Editor**: GIMP (GNU Image Manipulation Program)
- **Libraries**: GIMP Python API (PDB)

## How to Run the Script

1. Install GIMP from [gimp.org](https://www.gimp.org).
2. Clone or download this repository.
3. Install the required font (Black Knife Demo):
    - Double-click the `.ttf` file and select "Install Font."
    - Add the font to GIMP via Preferences > Folders > Fonts.
4. Open GIMP and navigate to Filters > Python-Fu > Console.
5. Load and execute the script in the Python-Fu console.
6. The poster will be generated with default settings, which you can customize within the script.

## Poster Details

### About the Artwork

This poster captures the essence of *The Garden Tantra*, reflecting the beauty of nature and spirituality. The artwork combines:

- **Norwegian and Indian Wildlife**: Featuring flora and fauna, including lush creepers, willow trees, and red deer.
- **Typography**: Title text in bright indigo for emphasis, contrasting against a minimal background.
- **Balance and Harmony**: A thoughtfully balanced composition with rhythmic placement of elements.

### Layers

- Background imagery
- Title and copyright text with shadows and highlights
- Wildlife elements

### Design Principles Applied

1. **Balance**: Visual weight is evenly distributed across the A4 canvas.
2. **Proximity**: Elements like creepers and willow trees form cohesive clusters.
3. **Alignment**: Subtle alignment guides the arrangement without strict symmetry.
4. **Unity**: Consistent artistic style integrates all components seamlessly.
5. **Emphasis**: Title text in bright indigo serves as the focal point.
6. **Rhythm**: Elements are arranged to guide the viewer’s eye naturally.

## Technical Details

### Text Formatting

- Sets text color, justification, and line spacing.
- Implements shadow effects and highlights for depth.

### Image Handling

- Supports PNG format with alpha transparency.
- Adjusts RGB_IMAGE to RGBA_IMAGE for layers with transparent parts.

### Script Structure

- **Layer Creation**: Automates layer setup for text and imagery.
- **Customization**: Modify text content, fonts, and colors directly in the script.

## Acknowledgments

Created with love, light, and rainbows. Inspired by *The Garden Tantra* by Vikram Kolmannskog.
