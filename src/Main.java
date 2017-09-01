import java.io.FileReader;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;

public class Main {
	public static void main(String[] args) throws Exception {
		ScriptEngine engine = (new ScriptEngineManager()).getEngineByName("JavaScript"); // nashorn
		engine.eval(new FileReader(args[0]));
	}
}