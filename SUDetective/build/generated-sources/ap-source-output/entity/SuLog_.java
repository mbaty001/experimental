package entity;

import entity.HwType;
import entity.NodeType;
import entity.Su;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.3.0.v20110604-r9504", date="2013-07-12T15:27:03")
@StaticMetamodel(SuLog.class)
public class SuLog_ { 

    public static volatile SingularAttribute<SuLog, HwType> hWTYPEidHWTYPE;
    public static volatile SingularAttribute<SuLog, Integer> logErrors;
    public static volatile SingularAttribute<SuLog, Integer> idSULOG;
    public static volatile SingularAttribute<SuLog, String> nodeName;
    public static volatile SingularAttribute<SuLog, Su> sUidSU;
    public static volatile SingularAttribute<SuLog, String> logFile;
    public static volatile SingularAttribute<SuLog, NodeType> nODETYPEidNODETYPE;

}