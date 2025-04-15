"""
SETTINGS MODULE DOCUMENTATION

This module contains all configurable game parameters including:
- Screen and display settings
- Game object properties
- Animation parameters
- Sound configuration
- Resource paths
- Debugging flags
"""

# ======================
# SCREEN AND FRAME SETTINGS
# ======================
SCREEN_WIDTH = 600        # Game window width in pixels
SCREEN_HEIGHT = 476       # Game window height in pixels
OBSTACLES_FRAMES = 3      # Number of animation frames for obstacles
FPS = 14                  # Target frames per second (game speed)

# ======================
# USER INTERFACE SETTINGS
# ======================
ENEMY_ICON_POS = (SCREEN_WIDTH - 100, 20)  # Position of enemy counter icon
SCORE_TEXT_OFFSET = 40    # Horizontal offset for score text from icon

# ======================
# COLOR SETTINGS
# ======================
COLOR_SCREEN_LOSE = (58, 35, 46)      # Background color for game over screen
TEXT_COLOR_LOSE = (137, 0, 0)         # Color for "Game Over" text
TEXT_COLOR_RESTART = (230, 243, 53)   # Color for restart prompt text

# ======================
# PLAYER CHARACTER SETTINGS
# ======================
PLAYER_START_X = 80       # Initial X position of player
PLAYER_START_Y = 360      # Initial Y position of player
PLAYER_SPEED = 8          # Horizontal movement speed (pixels/frame)
PLAYER_JUMP_COUNT = 5     # Vertical force applied when jumping
PLAYER_MOVE_LIMIT_LEFT = 50   # Left boundary for player movement
PLAYER_MOVE_LIMIT_RIGHT = 200 # Right boundary for player movement

# ======================
# ENEMY SETTINGS
# ======================
ENEMY_START_X = 620       # Initial X position (off-screen right)
ENEMY_START_Y = 360       # Initial Y position (same as player)
ENEMY_SPEED = 5           # Movement speed (pixels/frame)

# ======================
# PROJECTILE (BOTTLE) SETTINGS
# ======================
BOTTLE_SPEED = 10         # Horizontal travel speed
BOTTLE_LIFETIME = 3       # Seconds before bottle disappears
BOTTLE_COOLDOWN = 1       # Minimum seconds between throws

# ======================
# OBSTACLE SETTINGS
# ======================
OBSTACLE_SPEED = 5        # Movement speed (pixels/frame)
OBSTACLE_START_Y = 440    # Initial Y position (lower than player)
OBSTACLE_START_X = 800    # Initial X position (off-screen right)

# ======================
# ANIMATION SETTINGS
# ======================
PLAYER_ANIM_FRAMES = 6    # Number of animation frames for player
ENEMY_ANIM_FRAMES = 8     # Number of animation frames for enemies
BOTTLES_ANIM_FRAMES = 8   # Number of animation frames for bottles

# ======================
# SOUND SETTINGS
# ======================
BACKGROUND_MELODY = "sounds/background_melody.mp3"  # Background music file
BACKGROUND_MELODY_VOLUME = 0.01  # Volume level (0.0 to 1.0)

# ======================
# SPAWN TIMING SETTINGS
# ======================
# Enemy spawn time ranges (milliseconds)
ENEMY_SPAWN_MIN_TIME = 2000
ENEMY_SPAWN_MAX_TIME = 5000
ENEMY_SPAWN_STEP = 1000   # Randomization step size

# Obstacle spawn time ranges (milliseconds)
OBSTACLE_SPAWN_MIN_TIME = 2000
OBSTACLE_SPAWN_MAX_TIME = 4500
OBSTACLE_SPAWN_STEP = 800  # Randomization step size

# ======================
# RESOURCE PATHS
# ======================
ASSET_PATH = "images/"    # Base directory for game assets
ICON_PATH = ASSET_PATH + "icon.png"              # Game window icon
BACKGROUND_IMAGE_PATH = ASSET_PATH + "background.png"  # Background image
PLAYER_LEFT_PATH = ASSET_PATH + "player_movement_left/"  # Left movement frames
PLAYER_RIGHT_PATH = ASSET_PATH + "player_movement_right/" # Right movement frames
ENEMY_IMAGE_PATH = ASSET_PATH + "policeman_movement/"   # Enemy animation frames
BOTTLE_IMAGE_PATH = ASSET_PATH + "bottle_movement/"     # Bottle animation frames
OBSTACLE_IMAGE_PATH = ASSET_PATH + "obstacles/"        # Obstacle sprites
FONT_PATH = "fonts/VT323-Regular.ttf"  # Game font file
