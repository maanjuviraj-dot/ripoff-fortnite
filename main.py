# 3. Shooting Logic

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . 5 5 5 5 5 5 5 5 . . . . .
            . . . 5 5 5 5 5 5 5 5 . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        mySprite,
        200,
        0)
    # Make bullet fire in the direction you are moving
    projectile.vx = controller.dx() * 200
    projectile.vy = controller.dy() * 200
    # If standing still, shoot right by default
    if projectile.vx == 0 and projectile.vy == 0:
        projectile.vx = 200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# When an enemy touches you

def on_on_overlap(player2, bot):
    info.change_life_by(-1)
    bot.destroy(effects.disintegrate, 200)
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

# When your bullet hits an enemy

def on_on_overlap2(bullet, bot2):
    bullet.destroy()
    bot2.destroy(effects.fire, 100)
    # Keep track of your "Kills"
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

bot3: Sprite = None
projectile: Sprite = None
mySprite: Sprite = None
# --- Week 1: Player, Movement, and Basic Shooting ---
# 1. Setup Player
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . .
        . . . . f f f 2 2 f f f . . . .
        . . . f f f 2 2 2 2 f f f . . .
        . . f f f e e e e e e f f f . .
        . . f f e 2 2 2 2 2 2 e e f . .
        . . f e 2 f f f f f f 2 e f . .
        . . f f f f e e e e f f f f . .
        . f f e f b f 4 4 f b f e f f .
        . f e e 4 1 f d d f 1 4 e e f .
        . . f e e d d d d d d e e f . .
        . . . f e e 4 4 4 4 e e f . . .
        . . e 4 f 2 2 2 2 2 2 f 4 e . .
        . . 4 d f 2 2 2 2 2 2 f d 4 . .
        . . 4 4 f 4 4 5 5 4 4 f 4 4 . .
        . . . . . f f f f f f . . . . .
        . . . . . f f . . f f . . . . .
        """),
    SpriteKind.player)
# 2. Movement
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
scene.set_tile_map_level(tilemap("""
    level1
    """))
tiles.set_current_tilemap(tilemap("""
    level2
    """))
scene.camera_follow_sprite(mySprite)
# Spawn an enemy every 8 seconds

def on_update_interval():
    global bot3
    bot3 = sprites.create(img("""
            . . . . f f f f f . . . . . . .
            . . . f e e e e e f . . . . . .
            . . f d d d d e e e f . . . . .
            . c d f d d f d e e f f . . . .
            . c d f d d f d e e d d f . . .
            c d e e d d d d e e b d c . . .
            c d d d d c d d e e b d c . f f
            c c c c c d d d e e f c . f e f
            . f d d d d d e e f f . . f e f
            . . f f f f f e e e e f . f e f
            . . . . f e e e e e e e f f e f
            . . . f e f f e f e e e e f f .
            . . . f e f f e f e e e e f . .
            . . . f d b f d b f f e f . . .
            . . . f d d c d d b b d f . . .
            . . . . f f f f f f f f f . . .
            """),
        SpriteKind.enemy)
    # Pick a random spot on the grass (not on a wall!)
    tiles.place_on_random_tile(bot3, assets.tile("""
        transparency16
        """))
    # Make them chase you
    bot3.follow(mySprite, 40)
game.on_update_interval(8000, on_update_interval)
