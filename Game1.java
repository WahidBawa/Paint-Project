import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Game1 extends JFrame implements ActionListener, KeyListener {
	JButton nBut = new JButton("North");
	JButton eBut = new JButton("East");
	JButton sBut = new JButton("South");
	JButton wBut = new JButton("West");
	GamePanel game = new GamePanel();

	public Game1() {
		super("Move the Box");

		setSize(500,500);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		add(nBut, BorderLayout.NORTH);
		add(eBut, BorderLayout.EAST);
		add(sBut, BorderLayout.SOUTH);
		add(wBut, BorderLayout.WEST);
		add(game, BorderLayout.CENTER);

		nBut.addActionListener(this);
		eBut.addActionListener(this);
		sBut.addActionListener(this);
		wBut.addActionListener(this);
		addKeyListener(this);
		setVisible(true);
	}

	public void keyTyped(KeyEvent k) {}
	public void keyPressed(KeyEvent k) {
		// int key = k.getKeyCode();
		// if (key == KeyEvent.VK_ESCAPE) {
		// 	System.exit(0);
		// }
	}
	public void keyReleased(KeyEvent k) {}

	public void actionPerformed(ActionEvent evt) {
		Object source = evt.getSource();
		if (source == nBut)
			game.move(0,-10);
		if (source == sBut)
			game.move(0,10);
		if (source == eBut)
			game.move(10,0);
		if (source == wBut)
			game.move(-10,0);
		game.repaint();
	}

	public static void main(String[] args) {
		new Game1();
	}
}