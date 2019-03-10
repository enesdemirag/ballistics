extends Area2D
export (PackedScene) var Ball

export (int) var ball_count
var screensize

func _ready():
	randomize()
	$Music.play()
	screensize = get_viewport_rect().size
	$CannonPath/CannonSpawnLocation.set_offset(randi())
	$Cannon.position = $CannonPath/CannonSpawnLocation.position
	$Cannon.rotation = $CannonPath/CannonSpawnLocation.rotation + rand_range(PI / 10, 9 * PI / 10)
	print("Hello World")

func updateCannonRotation(rotation):
	$Cannon.rotation += rotation * PI / 180

func _process(delta):
	if $Cannon.rotation >= 9 * PI / 10:
		$Cannon.rotation -= PI / 90
	elif $Cannon.rotation <= PI / 10:
		$Cannon.rotation += PI / 90

func _physics_process(delta):
	if Input.is_action_just_released("ui_select"):
		if ball_count > 0:
			var ball = Ball.instance()
			add_child(ball)
			ball.position = $Cannon.position
			ball.rotation = $Cannon.rotation
			ball.set_linear_velocity(Vector2(400, 0).rotated($Cannon.rotation - PI))
			ball_count -= 1
	if Input.is_action_pressed("ui_right"):
		updateCannonRotation(1)
	if Input.is_action_pressed("ui_left"):
		updateCannonRotation(-1)

func _on_Target_hit():
	pass # Success
