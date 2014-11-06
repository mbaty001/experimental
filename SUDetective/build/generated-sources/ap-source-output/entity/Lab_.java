package entity;

import entity.HwType;
import entity.IpType;
import entity.Ms;
import entity.Su;
import entity.Ts;
import javax.annotation.Generated;
import javax.persistence.metamodel.ListAttribute;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.3.0.v20110604-r9504", date="2013-07-12T15:27:03")
@StaticMetamodel(Lab.class)
public class Lab_ { 

    public static volatile SingularAttribute<Lab, HwType> aCSTYPEidHWTYPE;
    public static volatile SingularAttribute<Lab, String> hap;
    public static volatile SingularAttribute<Lab, String> dualIp;
    public static volatile SingularAttribute<Lab, Integer> noOfLangs;
    public static volatile ListAttribute<Lab, Su> suList;
    public static volatile SingularAttribute<Lab, IpType> iPTYPEidIPTYPE;
    public static volatile SingularAttribute<Lab, String> name;
    public static volatile SingularAttribute<Lab, String> rms;
    public static volatile SingularAttribute<Lab, Integer> idLAB;
    public static volatile ListAttribute<Lab, Ts> tsList;
    public static volatile ListAttribute<Lab, Ms> msList;

}