extends Area2D
export (PackedScene) var Ball

export (int) var ball_count
var screensize
var initial_cannon_rotation

func _ready():
	randomize()
	print("Hello")
	$Music.play()
	screensize = get_viewport_rect().size
	$CannonPath/CannonSpawnLocation.set_offset(randi())
	$Cannon.position = $CannonPath/CannonSpawnLocation.position
	initial_cannon_rotation = $CannonPath/CannonSpawnLocation.rotation + PI / 2
	$Cannon.rotation = initial_cannon_rotation + rand_range(-PI / 2.5, PI / 2.5)

func updateCannonRotation(rotation):
	$Cannon.rotation += rotation * PI / 180

func _process(delta):
	if $Cannon.rotation >= 9 * PI / 10:
		$Cannon.rotation -= PI / 90
	elif $Cannon.rotation <= PI / 10:
		$Cannon.rotation += PI / 90

func _physics_process(delta):
	if Input.is_action_pressed("ui_select"):
		$BallTimer.start()
	if Input.is_action_pressed("ui_right"):
		updateCannonRotation(1)
	if Input.is_action_pressed("ui_left"):
		updateCannonRotation(-1)

func _on_BallTimer_timeout():
	if ball_count > 0:
		var ball = Ball.instance()
		add_child(ball)
		ball.position = $Cannon.position
		ball.rotation = $Cannon.rotation
		ball.set_linear_velocity(Vector2(400, 0).rotated($Cannon.rotation - PI))
		ball_count -= 1
	else:
		pass

func _on_Target_hit():
	pass # Success
