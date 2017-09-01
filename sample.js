print('Hello World');
var ServerSocket = java.net.ServerSocket; print(ServerSocket);
var barr = Java.type("byte[]"); print(barr);

var JFrame = Java.type("javax.swing.JFrame"); print(JFrame);
var frame = new JFrame(); print(frame);
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
frame.setTitle("Example GUI");
frame.setSize(320,240);
frame.setVisible(true);
