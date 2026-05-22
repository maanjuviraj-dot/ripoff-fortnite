// 3. Shooting Logic
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, mySprite, 200, 0)
    // Make bullet fire in the direction you are moving
    projectile.vx = controller.dx() * 200
    projectile.vy = controller.dy() * 200
    // If standing still, shoot right by default
    if (projectile.vx == 0 && projectile.vy == 0) {
        projectile.vx = 200
    }
})
// When an enemy touches you
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (player2, bot) {
    info.changeLifeBy(-1)
    bot.destroy(effects.disintegrate, 200)
    scene.cameraShake(4, 500)
})
// When your bullet hits an enemy
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (bullet, bot2) {
    bullet.destroy()
    bot2.destroy(effects.fire, 100)
    // Keep track of your "Kills"
    info.changeScoreBy(1)
})
let bot3: Sprite = null
let projectile: Sprite = null
let mySprite: Sprite = null
// --- Week 1: Player, Movement, and Basic Shooting ---
// 1. Setup Player
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
// 2. Movement
controller.moveSprite(mySprite)
scene.cameraFollowSprite(mySprite)
scene.setTileMapLevel(tilemap`
    level1
    `)
tiles.setCurrentTilemap(tilemap`level2`)
scene.cameraFollowSprite(mySprite)
// Spawn an enemy every 8 seconds
game.onUpdateInterval(2000, function () {
    bot3 = sprites.create(img`
        . . . . e e e e e . . . . . f . 
        . . . e f f f f f e . . . . . . 
        . . e d d d d f f f e . . . . . 
        . c e e d d e e f f f e . . . . 
        . c d e d d e d e f d d e . . . 
        c d e e d d d d e f b d c . . . 
        c d d d d c d d e f b d c . e e 
        c c c c c d d d e f f c . e f f 
        . f d d d d d e f f f . . e f f 
        . . e e e e e f f f f e . e f f 
        . . . e f f f f f f f e e f f e 
        . . . e f f f f f f f f f f e . 
        . . . e f f f f f f f f f e . . 
        . . . e d b f d b f f f e . . . 
        . . . e d d c d d b b d e . . . 
        . . . e e e e e e e e e e . . . 
        `, SpriteKind.Enemy)
    // Pick a random spot on the grass (not on a wall!)
    tiles.placeOnRandomTile(bot3, assets.tile`transparency16`)
    // Make them chase you
    bot3.follow(mySprite, 40)
})
