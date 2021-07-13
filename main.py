@namespace
class SpriteKind:
    floor = SpriteKind.create()

def on_overlap_tile(sprite, location):
    if play.tile_kind_at(TileDirection.LEFT, assets.tile("""
        myTile0
    """)):
        info.change_score_by(-1)
    if play.tile_kind_at(TileDirection.RIGHT, assets.tile("""
        myTile0
    """)):
        info.change_score_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite, location):
    tiles.set_tile_at(tiles.get_tile_location(29, 10),
        assets.tile("""
            wall
        """))
    tiles.set_wall_at(tiles.get_tile_location(29, 10), False)
    tiles.set_wall_at(tiles.get_tile_location(29, 9), False)
    tiles.set_wall_at(tiles.get_tile_location(29, 8), False)
    tiles.set_wall_at(tiles.get_tile_location(29, 7), False)
    tiles.set_wall_at(tiles.get_tile_location(29, 6), False)
    tiles.set_tile_at(tiles.get_tile_location(19, 12),
        assets.tile("""
            transparency16
        """))
    music.power_up.play()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile2)

def on_a_pressed():
    global jumpcounter
    if jumpcounter <= 1:
        play.vy = -100
        play.ay = 170
        jumpcounter += 1
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

jumpcounter = 0
play: Sprite = None
scene.set_background_color(1)
play = sprites.create(img("""
        3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    """),
    SpriteKind.player)
jumpcounter = 0
controller.move_sprite(play, 100, 0)
tiles.set_tilemap(tilemap("""
    level1
"""))
play.vy = 150
scene.camera_follow_sprite(play)
info.set_life(3)

def on_on_update():
    global jumpcounter
    if play.is_hitting_tile(CollisionDirection.BOTTOM):
        jumpcounter = 0
game.on_update(on_on_update)
