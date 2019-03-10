extends RigidBody2D

export (int) var min_speed
export (int) var max_speed

func _ready():
	$KillTimer.start()

func _on_KillTimer_timeout():
	queue_free()