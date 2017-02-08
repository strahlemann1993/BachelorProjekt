import java.io.File;
import java.util.Timer;
import java.util.TimerTask;

public class CommandLineTimer {
	int INTERVAL = 1000*5;

	public static void main(String[] args) {
	 new CommandLineTimer();
	}

	public CommandLineTimer(){
		while (true){
			if (this.isCamSwitchOn())
				doStuff();
			try {
				Thread.sleep(INTERVAL);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}

private boolean isCamSwitchOn() {
	    File file = new File("/opt/openhab/webapps/cameras/kameraAn");
	    if (file.exists()){
	    	return true;
	    }
	    else return false;
	}

public void doStuff(){
	Runtime rt = Runtime.getRuntime();
	try{
		Process pr = rt.exec("fswebcam -r 1280x720 /opt/openhab/webapps/cameras/image");
                pr.waitFor();
		}
		catch (Exception e){
			e.printStackTrace();
		}
		}
}
