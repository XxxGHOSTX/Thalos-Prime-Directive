# 3D Neural Grid Interface

## Overview

The Thalos Prime v3.0 3D Neural Grid Interface provides an immersive, cyberpunk-style visualization of the Synthetic Biological Intelligence system. This interface features an animated particle system that represents neural activity in a visually striking manner.

## Features

- **3D Particle System**: 3000 animated particles with depth-based perspective
- **Real-time Telemetry**: Live display of system metrics (SBI_LATENCY and NEURAL_LOAD)
- **Matrix-Style Aesthetic**: Green-on-black color scheme with glowing effects
- **Responsive Design**: Automatically adapts to window size changes
- **Performance Optimized**: Efficient Canvas-based rendering

## Implementation Details

### Technology Stack

- **HTML5 Canvas**: Used for rendering the particle system
- **Vanilla JavaScript**: No external dependencies required
- **CSS3 Animations**: For telemetry status indicators

### Particle System

The particle system simulates a 3D neural grid with the following characteristics:

- **Particle Count**: 3000 particles
- **3D Space**: Particles exist in a virtual 3D space with x, y, z coordinates
- **Depth Perspective**: Particles closer to the viewer (higher z-value) appear larger and more opaque
- **Movement**: Particles move continuously to create a flowing effect
- **Fade Trails**: Semi-transparent trails create a sense of motion

### Telemetry Display

The interface displays four key metrics:

1. **SYSTEM**: Shows "THALOS PRIME V3.0"
2. **STATUS**: Displays "OPERATIONAL" with blinking animation
3. **SBI_LATENCY**: Simulated latency values (0-0.05ms)
4. **NEURAL_LOAD**: Simulated neural load percentage (10-30%)

*Note: Telemetry values in this interface are simulated for visualization purposes.*

## Usage

### Accessing the Interface

The 3D Neural Grid Interface is served as the default interface when accessing the Thalos Prime web server:

```bash
python src/interfaces/web/web_server.py
```

Then navigate to: `http://localhost:8000`

### File Location

- **Template**: `src/interfaces/web/templates/thalos_3d_interface.html`
- **Web Server**: `src/interfaces/web/web_server.py`

## Customization

### Adjusting Particle Count

To modify the number of particles for performance or visual preference, edit line 99 in `thalos_3d_interface.html`:

```javascript
for (let i = 0; i < 3000; i++) {  // Change 3000 to desired count
    particles.push(new Particle());
}
```

### Modifying Colors

The default color scheme is Matrix green (#0f0). To change colors, modify the RGB values in the particle rendering:

```javascript
ctx.fillStyle = `rgba(0, 255, 0, ${opacity})`;  // Change (0, 255, 0) for different colors
```

### Adjusting Animation Speed

Modify the velocity ranges in the Particle class `reset()` method:

```javascript
this.vx = (Math.random() - 0.5) * 0.5;  // Increase multiplier for faster movement
this.vy = (Math.random() - 0.5) * 0.5;
this.vz = (Math.random() - 0.5) * 2;
```

## Performance Considerations

- **Particle Count**: 3000 particles provides good visual effect with acceptable performance on modern devices
- **Canvas Clearing**: Uses semi-transparent black fill for trail effects instead of full clear
- **No Shadow Blur**: Removed expensive shadow blur effects for better performance
- **Efficient Updates**: Only updates telemetry values probabilistically

## Browser Compatibility

- **Modern Browsers**: Chrome, Firefox, Safari, Edge (latest versions)
- **Requirements**: HTML5 Canvas support, JavaScript enabled
- **Mobile**: Responsive and works on mobile devices (may reduce particle count for optimal performance)

## Future Enhancements

Potential improvements for future versions:

1. **Dynamic Particle Count**: Adjust based on device capabilities
2. **Real Telemetry Integration**: Connect to actual backend metrics
3. **Interactive Elements**: Allow user interaction with particles
4. **WebGL Version**: Implement true 3D rendering with Three.js when available
5. **Customizable Themes**: Allow users to change color schemes
6. **Data Visualization**: Map real neural network activity to particle behavior

## Troubleshooting

### Particles Not Visible

If particles are not visible, check:
- Canvas element is present in DOM
- JavaScript console for errors
- Canvas size is properly set
- Browser supports HTML5 Canvas

### Performance Issues

If experiencing lag or stuttering:
- Reduce particle count (try 1500-2000)
- Increase fade rate for less trail rendering
- Close other browser tabs
- Check CPU usage

## Credits

Implementation based on the Thalos Prime v3.0 Synthetic Biological Intelligence system architecture.
