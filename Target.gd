extends RigidBody2D

signal hit

func _ready():
	pass

func _on_Target_body_entered(body):
	hide()
	emit_signal("hit")