# tf-graph-visualiser


Assuming, that tf_session is a tf.Session() object.<br>

Usage:<br><br>

ipdb> node_to_display = tf_session.graph.get_tensor_by_name('softmax:0')<br>
ipdb> from nodedisplay import draw<br>
ipdb> draw(node_to_display, tf_session, 'inception_v3_net')<br>
