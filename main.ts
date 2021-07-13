namespace SpriteKind {
    export const floor = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite, location) {
    tiles.setTileAt(tiles.getTileLocation(29, 10), assets.tile`wall`)
    tiles.setWallAt(tiles.getTileLocation(29, 10), false)
    tiles.setWallAt(tiles.getTileLocation(29, 9), false)
    tiles.setWallAt(tiles.getTileLocation(29, 8), false)
    tiles.setWallAt(tiles.getTileLocation(29, 7), false)
    tiles.setWallAt(tiles.getTileLocation(29, 6), false)
    tiles.setTileAt(tiles.getTileLocation(19, 12), assets.tile`transparency16`)
    music.powerUp.play()
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (jumpcounter <= 1) {
        play.vy = -100
        play.ay = 170
        jumpcounter += 1
    }
})
let PlayFacingLeft = false
let jumpcounter = 0
let play: Sprite = null
scene.setBackgroundColor(1)
play = sprites.create(assets.image`PlayAlienIdle`, SpriteKind.Player)
jumpcounter = 0
controller.moveSprite(play, 100, 0)
tiles.setTilemap(tilemap`level1`)
play.vy = 150
scene.cameraFollowSprite(play)
info.setLife(3)
let badguy = sprites.create(assets.tile`myTile0`, SpriteKind.Enemy)
badguy.setPosition(140, 235)
badguy.setVelocity(50, 0)
badguy.setBounceOnWall(true)
game.onUpdate(function () {
    if (play.isHittingTile(CollisionDirection.Bottom)) {
        jumpcounter = 0
    }
    if (play.vx > 0) {
        PlayFacingLeft = true
    } else if (play.vx < 0) {
        PlayFacingLeft = false
    }
    if (play.vy > 0) {
        play.setImage(assets.image`PlayAlienFall`)
    } else if (play.vy < 0) {
        play.setImage(assets.image`PlayAlienJump`)
    } else {
        play.setImage(assets.image`PlayAlienIdle`)
    }
})
